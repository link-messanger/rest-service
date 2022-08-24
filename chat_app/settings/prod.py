import os

from .settings import *

SECRET_KEY = os.environ['SECRET_KEY']


DEBUG = False

ALLOWED_HOSTS = ['amir-chatapp.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "DATABASE_URL": os.environ['DATABASE_URL'],
    }
}
