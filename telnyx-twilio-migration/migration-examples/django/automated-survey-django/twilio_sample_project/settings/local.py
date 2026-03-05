import environ

environ.Env.read_env('.env')

from .common import *

ALLOWED_HOSTS = ['127.0.0.1']
