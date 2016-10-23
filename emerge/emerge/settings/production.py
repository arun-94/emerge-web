# -*- coding: utf-8 -*-
from .base import *
import dj_database_url

DEBUG = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLOWED_HOSTS = ['yourappname.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)