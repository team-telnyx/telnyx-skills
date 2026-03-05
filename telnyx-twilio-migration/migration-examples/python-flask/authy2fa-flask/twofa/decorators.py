from flask import abort, flash, redirect, request, session, url_for
from functools import wraps

from .models import User


def login_required(f):
    """Redirects requests to /login if the user isn't authenticated"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id', None)
        if user_id:
            user = User.query.filter_by(id=user_id).one_or_none()
            if user is not None:
                return f(*args, **kwargs)

        flash('Please log in before accessing that page.', 'info')
        return redirect(url_for('auth.log_in'))

    return decorated_function


def login_verified(f):
    """
    Redirects requests if the current user has not verified their login with
    Authy
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id', False)
        if user_id:
            user = User.query.filter_by(id=user_id).one_or_none()
            if user is not None and user.authy_status == 'approved':
                return f(*args, **kwargs)

        flash(
            'You must complete your login before accessing that page.', 'info'
        )  # noqa: E501
        return redirect(url_for('auth.log_in'))

    return decorated_function


def verify_authy_request(f):
    """
    Verifies that a OneTouch callback request came from Authy
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the request URL without the parameters
        from .utils import get_authy_client

        client = get_authy_client()

        response = client.one_touch.validate_one_touch_signature(
            request.headers['X-Authy-Signature'],
            request.headers['X-Authy-Signature-Nonce'],
            request.method,
            request.url,
            request.json,
        )
        if response:
            # The two signatures match - this request is authentic
            return f(*args, **kwargs)

        # The signatures didn't match - abort this request
        return abort(400)

    return decorated_function
