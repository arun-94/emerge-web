# -*- coding: utf-8 -*-
from .base import *
import dj_database_url

DEBUG = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLOWED_HOSTS = ['emerge-webapi.herokuapp.com']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
