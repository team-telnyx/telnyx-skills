from authy.api import AuthyApiClient
from flask import current_app
from authy import AuthyApiException
import telnyx


def get_authy_client():
    """ Return a configured Authy client. """
    return AuthyApiClient(current_app.config['AUTHY_API_KEY'])


def get_telnyx_client():
    """Return a configured Telnyx client."""
    telnyx.api_key = current_app.config['TELNYX_API_KEY']
    return telnyx


def create_user(form):
    """Creates an Authy user and then creates a database User"""
    client = get_authy_client()

    # Create a new Authy user with the data from our form
    authy_user = client.users.create(
        form.email.data, form.phone_number.data, form.country_code.data
    )

    # If the Authy user was created successfully, create a local User
    # with the same information + the Authy user's id
    if authy_user.ok():
        return form.create_user(authy_user.id)
    else:
        raise AuthyApiException('', '', authy_user.errors()['message'])


def send_authy_token_request(authy_user_id):
    """
    Sends a request to Telnyx to send a SMS verification code to a user's phone.
    Falls back to Authy if Telnyx is not configured.
    """
    # Try Telnyx first for SMS verification
    telnyx_api_key = current_app.config.get('TELNYX_API_KEY')
    verify_profile_id = current_app.config.get('TELNYX_VERIFY_PROFILE_ID')
    
    if telnyx_api_key and verify_profile_id:
        telnyx.api_key = telnyx_api_key
        # Get the user to find their phone number
        authy_client = get_authy_client()
        user_status = authy_client.users.status(authy_user_id)
        if user_status.ok():
            phone_number = user_status.content.get('phone_number')
            if phone_number:
                telnyx.verifications.trigger_sms(
                    phone_number=phone_number,
                    verify_profile_id=verify_profile_id
                )
                return
    
    # Fallback to Authy SMS
    client = get_authy_client()
    client.users.request_sms(authy_user_id)


def send_authy_one_touch_request(authy_user_id, email=None):
    """Initiates an Authy OneTouch request for a user"""
    client = get_authy_client()

    details = {}

    if email:
        details['Email'] = email

    response = client.one_touch.send_request(
        authy_user_id, 'Request to log in to Telnyx demo app', details=details
    )

    if response.ok():
        return response.content


def verify_authy_token(authy_user_id, user_entered_code):
    """Verifies a user-entered token with Telnyx Verify (or Authy as fallback)"""
    # Try Telnyx first for SMS verification
    telnyx_api_key = current_app.config.get('TELNYX_API_KEY')
    verify_profile_id = current_app.config.get('TELNYX_VERIFY_PROFILE_ID')
    
    if telnyx_api_key and verify_profile_id:
        telnyx.api_key = telnyx_api_key
        # Get the user to find their phone number
        authy_client = get_authy_client()
        user_status = authy_client.users.status(authy_user_id)
        if user_status.ok():
            phone_number = user_status.content.get('phone_number')
            if phone_number:
                try:
                    result = telnyx.verifications.by_phone_number(
                        phone_number
                    ).verify(
                        code=str(user_entered_code),
                        verify_profile_id=verify_profile_id
                    )
                    # Telnyx uses 'accepted' not 'approved'
                    if result.data.response_code == 'accepted':
                        # Return a mock-like response for compatibility
                        return type('obj', (object,), {
                            'ok': lambda: True,
                            'content': {'status': 'approved'}
                        })()
                    else:
                        return type('obj', (object,), {
                            'ok': lambda: False,
                            'content': {'status': 'rejected'}
                        })()
                except Exception:
                    pass  # Fall back to Authy
    
    # Fallback to Authy token verification
    client = get_authy_client()
    return client.tokens.verify(authy_user_id, user_entered_code)


def authy_user_has_app(authy_user_id):
    """Verifies a user has the Authy app installed"""
    client = get_authy_client()
    authy_user = client.users.status(authy_user_id)
    try:
        return authy_user.content['status']['registered']
    except KeyError:
        return False
