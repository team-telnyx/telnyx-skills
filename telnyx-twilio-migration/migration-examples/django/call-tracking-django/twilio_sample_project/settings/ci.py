'''
Test settings

- Run in Debug mode
'''

from .common import *  # noqa

# Turn on DEBUG for tests
DEBUG = True

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": "call_tracking",
        "USER": "postgres",
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
