# -*- coding: utf-8 -*-

import os

PROJECT_DIR = os.path.join(os.path.dirname(__file__), '..')
location = lambda x: os.path.join(PROJECT_DIR, x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Gabriel Freitas', 'gabrielfreitas@gmail.com'),
    ('Gustavo Carvalho', 'gt.salles@gmail.com')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pugpi',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

TIME_ZONE = 'America/Fortaleza'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = location('media')

MEDIA_URL = '/media/'

STATIC_ROOT = location('static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    location('media/static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'ahc1u5ri5320s)f2yjotia4!^x$cwnl1)6m3a(p9=!twtor#tj'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pugpi.urls'

WSGI_APPLICATION = 'pugpi.wsgi.application'

TEMPLATE_DIRS = (
    location('templates'),
)

INSTALLED_APPS = (
    'south',
    'suit',
    'taggit',
    'ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'apps.core',
    'apps.multimidia',
    'apps.news',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#CKEditor
CKEDITOR_UPLOAD_PATH = location('media/uploads')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'SpellChecker', 'Scayt']},
            {'name': 'clipboard',  'items': ['PasteText', '-', 'Undo', 'Redo' ]},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar', 'PageBreak', 'Iframe']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            '/',
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-',
                                              'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote',
                                            'CreateDiv',
            '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        ],
        'height': 300,
        'width': 710,
    },
}