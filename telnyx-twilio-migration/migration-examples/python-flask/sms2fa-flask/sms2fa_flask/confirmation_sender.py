from telnyx import Telnyx
from flask import current_app, session
import random


def send_confirmation_code(to_number):
    verification_code = generate_code()
    send_sms(to_number, verification_code)
    session['verification_code'] = verification_code
    return verification_code


def generate_code():
    return str(random.randrange(100000, 999999))


def send_sms(to_number, body):
    api_key = current_app.config.get('TELNYX_API_KEY')
    telnyx_phone_number = current_app.config.get('TELNYX_PHONE_NUMBER')
    messaging_profile_id = current_app.config.get('TELNYX_MESSAGING_PROFILE_ID')
    
    if not api_key or not telnyx_phone_number:
        raise ValueError("TELNYX_API_KEY and TELNYX_PHONE_NUMBER must be configured")
    
    # Create Telnyx client
    client = Telnyx(api_key=api_key)
    
    try:
        # Format the message text
        # Phone numbers should be formatted as E.164
        to_e164 = to_number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        
        message_params = {
            'from_': telnyx_phone_number,
            'to': to_e164,
            'text': body,
        }
        
        # Include messaging_profile_id if available
        if messaging_profile_id:
            message_params['messaging_profile_id'] = messaging_profile_id
            
        message = client.messages.send(**message_params)
        current_app.logger.info(f"SMS sent via Telnyx. Response: {message}")
        return message
    except Exception as e:
        current_app.logger.error(f"Error sending SMS via Telnyx: {str(e)}")
        raise
