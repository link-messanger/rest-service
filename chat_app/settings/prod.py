import os

import dj_database_url

from .settings import *

SECRET_KEY = os.environ['SECRET_KEY']


DEBUG = False

ALLOWED_HOSTS = ['amir-chatapp.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}
