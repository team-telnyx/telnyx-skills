import os

from dotenv import load_dotenv

load_dotenv()


class DefaultConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'not-so-secret')
    AUTHY_API_KEY = os.environ.get('AUTHY_API_KEY')
    TELNYX_API_KEY = os.environ.get('TELNYX_API_KEY')
    TELNYX_VERIFY_PROFILE_ID = os.environ.get('TELNYX_VERIFY_PROFILE_ID')
    db_path = os.path.join(os.path.dirname(__file__), 'authy2fa.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class TestingConfig(DefaultConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config_classes = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': DefaultConfig,
}
