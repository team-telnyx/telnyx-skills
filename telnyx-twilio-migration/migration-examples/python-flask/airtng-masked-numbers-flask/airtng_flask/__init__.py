import os
from airtng_flask.config import config_env_files
from flask import Flask

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(
    config_name='development', p_db=db, p_bcrypt=bcrypt, p_login_manager=login_manager
):
    new_app = Flask(__name__)
    config_app(config_name, new_app)

    p_db.init_app(new_app)
    p_bcrypt.init_app(new_app)
    p_login_manager.init_app(new_app)
    p_login_manager.login_view = 'register'
    return new_app


def config_app(config_name, new_app):
    new_app.config.from_object(config_env_files[config_name])
    
    # Ensure required config values are set from environment
    new_app.config['TELNYX_API_KEY'] = os.environ.get('TELNYX_API_KEY', '')
    new_app.config['TELNYX_PHONE_NUMBER'] = os.environ.get('TELNYX_PHONE_NUMBER', '')
    new_app.config['TELNYX_MESSAGING_PROFILE_ID'] = os.environ.get('TELNYX_MESSAGING_PROFILE_ID', '')
    new_app.config['TELNYX_CONNECTION_ID'] = os.environ.get('TELNYX_CONNECTION_ID', '')
    new_app.config['TELNYX_PUBLIC_KEY'] = os.environ.get('TELNYX_PUBLIC_KEY', '')


app = create_app()

import airtng_flask.views  # noqa F402
