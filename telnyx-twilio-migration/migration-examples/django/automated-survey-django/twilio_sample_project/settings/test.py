import environ

environ.Env.read_env('.env.test')

from .common import *
