import environ

environ.Env.read_env('.env')

from .common import *  # noqa
