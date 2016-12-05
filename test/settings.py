# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import os
from tempfile import mkdtemp

SECRET_KEY = "Please do not spew DeprecationWarnings"

# Haystack settings for running tests.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',

    'haystack',
    'test.core',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
            ]
        },
    },
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'test.core.urls'

HAYSTACK_ROUTERS = ['haystack.routers.DefaultRouter']

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'test.mocks.MockEngine',
    },
    'elasticsearch': {
        'ENGINE': 'elasticsearch2_backend.ElasticsearchSearchEngine',
        'URL': os.environ.get('TEST_ELASTICSEARCH_1_URL', 'http://localhost:9200/'),
        'INDEX_NAME': 'test_default',
        'INCLUDE_SPELLING': True,
    },
}
