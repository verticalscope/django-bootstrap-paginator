
import os
BASE_DIR = os.path.dirname(__file__)

DEBUG = True

INSTALLED_APPS = (
    'bootstrap_paginator',
    'testlist',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

SECRET_KEY = 'notsecure'

ROOT_URLCONF = 'urls'
