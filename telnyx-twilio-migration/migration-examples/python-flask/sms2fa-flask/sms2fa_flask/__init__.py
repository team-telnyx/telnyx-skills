from sms2fa_flask.config import config_env_files
from sms2fa_flask.models import db, User
from flask import Flask

from flask_login import LoginManager
from flask_session import Session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
login_manager = LoginManager()


def prepare_app(environment='development', p_db=db):
    app.config.from_object(config_env_files[environment])
    login_manager.init_app(app)
    p_db.init_app(app)
    
    # Initialize session with the same SQLAlchemy instance
    app.config['SESSION_SQLALCHEMY'] = db
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    sess = Session(app)
    
    with app.app_context():
        db.create_all()
    from . import views
    return app


def save_and_commit(item):
    db.session.add(item)
    db.session.commit()
db.save = save_and_commit


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
