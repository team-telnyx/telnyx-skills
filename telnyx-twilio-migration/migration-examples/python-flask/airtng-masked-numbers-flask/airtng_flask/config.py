import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    TELNYX_API_KEY = os.environ.get('TELNYX_API_KEY', None)
    TELNYX_PUBLIC_KEY = os.environ.get('TELNYX_PUBLIC_KEY', None)
    TELNYX_PHONE_NUMBER = os.environ.get('TELNYX_PHONE_NUMBER', None)
    TELNYX_MESSAGING_PROFILE_ID = os.environ.get('TELNYX_MESSAGING_PROFILE_ID', None)
    TELNYX_CONNECTION_ID = os.environ.get('TELNYX_CONNECTION_ID', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    TESTING = True
    LOGIN_DISABLED = True
    WTF_CSRF_ENABLED = False


config_env_files = {
    'testing': 'airtng_flask.config.TestConfig',
    'development': 'airtng_flask.config.DevelopmentConfig',
}
