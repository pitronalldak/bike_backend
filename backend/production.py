from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bikeforsale',
        'USER': 'petr_ryabinin',
        'PASSWORD': 'alesia',
        'HOST': '',
        'PORT': '',
    }
}

FRONTEND_URL = 'http://bikeforsale.ru'
BACKEND_URL = 'http://bikeforsale.ru'

ALLOWED_HOSTS = ['*']
