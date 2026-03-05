'''
Test settings

- Run in Debug mode
- Use SQLite for easy testing
'''

from .common import *  # noqa

# Turn on DEBUG for tests
DEBUG = True

# Use SQLite for local testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/db.sqlite3',
    }
}

# Allow all hosts for local testing
ALLOWED_HOSTS = ['*']

# Override the connection id requirement for testing
def check_required(field, msg):
    pass

# Skip the connection_id check during settings load
TELNYX_CONNECTION_ID = os.environ.get('TELNYX_CONNECTION_ID', 'test-connection-id')
