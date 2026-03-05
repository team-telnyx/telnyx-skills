from authy import AuthyApiException
from flask import flash, jsonify, redirect, render_template, request, session, url_for

from . import auth
from .forms import LoginForm, SignUpForm, VerifyForm
from ..database import db
from ..decorators import login_required, verify_authy_request
from ..models import User
from ..utils import create_user, send_authy_token_request, verify_authy_token


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """Powers the new user form"""
    form = SignUpForm(request.form)

    if form.validate_on_submit():
        try:
            user = create_user(form)
            session['user_id'] = user.id

            return redirect(url_for('main.account'))

        except AuthyApiException as e:
            form.errors['Authy API'] = [
                'There was an error creating the Authy user',
                e.msg,
            ]

    return render_template('signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def log_in():
    """
    Powers the main login form.

    - GET requests render the username / password form
    - POST requests process the form data via an AJAX request triggered in the
      user's browser
    """
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            session['user_id'] = user.id

            if user.has_authy_app:
                # Send a request to verify this user's login with OneTouch
                one_touch_response = user.send_one_touch_request()
                return jsonify(one_touch_response)
            else:
                return jsonify({'success': False})
        else:
            # The username and password weren't valid
            form.email.errors.append(
                'The username and password combination you entered are invalid'
            )

    if request.method == 'POST':
        # This was an AJAX request, and we should return any errors as JSON
        return jsonify(
            {'error': render_template('_login_error.html', form=form)}
        )  # noqa: E501
    else:
        return render_template('login.html', form=form)


@auth.route('/authy/callback', methods=['POST'])
@verify_authy_request
def authy_callback():
    """Authy uses this endpoint to tell us the result of a OneTouch request"""
    authy_id = request.json.get('authy_id')
    # When you're configuring your Endpoint/URL under OneTouch settings '1234'
    # is the preset 'authy_id'
    if authy_id != 1234:
        user = User.query.filter_by(authy_id=authy_id).one()

        if not user:
            return ('', 404)

        user.authy_status = request.json.get('status')
        db.session.add(user)
        db.session.commit()

    return ('', 200)


@auth.route('/login/status')
def login_status():
    """
    Used by AJAX requests to check the OneTouch verification status of a user
    """
    user = User.query.get(session['user_id'])
    return user.authy_status


@auth.route('/verify', methods=['GET', 'POST'])
@login_required
def verify():
    """Powers token validation (not using OneTouch)"""
    form = VerifyForm(request.form)
    user = User.query.get(session['user_id'])

    # Send a token to our user when they GET this page
    if request.method == 'GET':
        send_authy_token_request(user.authy_id)

    if form.validate_on_submit():
        user_entered_code = form.verification_code.data

        verified = verify_authy_token(user.authy_id, str(user_entered_code))
        if verified.ok():
            user.authy_status = 'approved'
            db.session.add(user)
            db.session.commit()

            flash(
                "You're logged in! Thanks for using two factor verification.", 'success'
            )  # noqa: E501
            return redirect(url_for('main.account'))
        else:
            form.errors['verification_code'] = ['Code invalid - please try again.']

    return render_template('verify.html', form=form)


@auth.route('/resend', methods=['POST'])
@login_required
def resend():
    """Resends a verification token to a user"""
    user = User.query.get(session.get('user_id'))
    send_authy_token_request(user.authy_id)
    flash('I just re-sent your verification code - enter it below.', 'info')
    return redirect(url_for('auth.verify'))


@auth.route('/logout')
def log_out():
    """Log out a user, clearing their session variables"""
    user_id = session.pop('user_id', None)
    user = User.query.get(user_id)
    user.authy_status = 'unverified'
    db.session.add(user)
    db.session.commit()

    flash("You're now logged out! Thanks for visiting.", 'info')
    return redirect(url_for('main.home'))
