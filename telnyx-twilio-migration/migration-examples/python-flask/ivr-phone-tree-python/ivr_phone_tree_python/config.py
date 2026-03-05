class DefaultConfig(object):
    DEBUG = False


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class TestConfig(DefaultConfig):
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


config_env_files = {
    'test': 'ivr_phone_tree_python.config.TestConfig',
    'development': 'ivr_phone_tree_python.config.DevelopmentConfig',
}
