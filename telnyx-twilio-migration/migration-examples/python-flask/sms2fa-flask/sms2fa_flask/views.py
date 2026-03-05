from flask import render_template, request, url_for, flash, redirect, session, current_app
from flask import abort
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from . import app
from .models import User
from .forms import LoginForm, SignUpForm
from .confirmation_sender import send_confirmation_code


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/secret-page')
@login_required
def secret_page():
    return render_template('secrets.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User.save_from_dict(form.as_dict)
        session['user_email'] = user.email
        send_confirmation_code(user.international_phone_number)
        return redirect(url_for('confirmation'))
    return render_template('signup.html', form=form)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user and user.is_password_valid(form.password.data):
            session['user_email'] = user.email
            send_confirmation_code(user.international_phone_number)
            return redirect(url_for('confirmation'))
        flash('Wrong user/password.', 'error')

    return render_template('sign_in.html', form=form)


@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    user = User.query.get(session.get('user_email', '')) or abort(401)

    if request.method == 'POST':
        if request.form['verification_code'] == session.get('verification_code'):
            login_user(user)
            return redirect(url_for('secret_page'))
        flash('Wrong code. Please try again.', 'error')

    return render_template('confirmation.html', user=user)


@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('root'))


@app.route('/health')
def health():
    """Health check endpoint for runtime testing."""
    return {'status': 'ok', 'telnyx_configured': bool(current_app.config.get('TELNYX_API_KEY'))}


@app.route('/test-sms/<phone_number>')
def test_sms(phone_number):
    """Test endpoint to send an SMS directly."""
    try:
        message = send_confirmation_code(phone_number)
        return {
            'status': 'success',
            'message_id': message.id if hasattr(message, 'id') else str(message),
            'to': phone_number,
            'code_sent': session.get('verification_code')
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 500
