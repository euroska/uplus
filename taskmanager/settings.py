# -*- coding: utf-8 -*-
import os
DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SECRET_KEY = ')dq%h#fuqfr-zt8#o=_o&*6r^(=g-3o*6p4mi8--z_8n@3x2*#'

# Application definition
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'taskmanager',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'taskmanager.middleware.AuthMiddleware',
]

ROOT_URLCONF = 'taskmanager.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'taskmanager.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

LANGUAGE_CODE = 'cs'
TIME_ZONE = 'UTC'
USE_I18N = True

USE_L10N = True
USE_TZ = True
LOGIN_URL = '/admin/login'
LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'taskmanager': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'taskmanager.log',
            'formatter': 'taskmanager',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    },
}
