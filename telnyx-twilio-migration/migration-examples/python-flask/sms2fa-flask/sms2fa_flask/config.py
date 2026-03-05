import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = 'secret-key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'default.sqlite'))
    
    # Telnyx Configuration (migrated from Twilio)
    TELNYX_API_KEY = os.environ.get('TELNYX_API_KEY', None)
    TELNYX_PHONE_NUMBER = os.environ.get('TELNYX_PHONE_NUMBER', None)
    TELNYX_MESSAGING_PROFILE_ID = os.environ.get('TELNYX_MESSAGING_PROFILE_ID', None)
    SESSION_TYPE = 'sqlalchemy'
    
    # Disable track modifications to avoid warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'dev.sqlite'))


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'test.sqlite'))
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    # Telnyx test config (migrated from Twilio)
    TELNYX_API_KEY = 'test_api_key'
    TELNYX_PHONE_NUMBER = '+15551230987'
    TELNYX_MESSAGING_PROFILE_ID = 'test_profile_id'

config_env_files = {
    'test': 'sms2fa_flask.config.TestConfig',
    'development': 'sms2fa_flask.config.DevelopmentConfig',
}
