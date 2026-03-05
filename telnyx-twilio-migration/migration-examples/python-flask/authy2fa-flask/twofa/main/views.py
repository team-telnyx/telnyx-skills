from flask import render_template, session

from . import main
from ..decorators import login_verified
from ..models import User


@main.route('/')
def home():
    return render_template("index.html")


@main.route('/account')
@login_verified
def account():
    """A sample user account page. Only accessible to logged in users"""
    user = User.query.get(session['user_id'])
    return render_template('account.html', user=user)
