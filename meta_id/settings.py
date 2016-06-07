# -*- coding: utf-8 -*-

"""
Django settings for meta-id project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import raven

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Aviso: Tenta obter uma chave através de uma variavél de ambiente
# Caso não encontre, utiliza uma chave de 49 caracteres gerada automaticamente
# durante a criação do projeto.
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'x@4$z5(ynk6gaza@h+2e&8v_&vy^8wznx#0*f6e+%bwz5rvxzv'
)

# AVISO: Não execute sua aplicação em produção com o DEBUG ligado.
# O padrão é False(Desligado), sendo necessário setar a variável META_ID_DEBUG
# como True para que o DEBUG passe a funcionar.
DEBUG = os.getenv(
    'DEBUG',
    False
)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [os.getenv('META_ID_DOMAIN', 'localhost')]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'oauth2_provider',
    'rest_framework',
    'rest_localflavor',
    'debug_toolbar',
    'widget_tweaks',
    'test_without_migrations',

    'meta_id.authentication',
    'meta_id.core',
    'meta_id.analise',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'meta_id.urls'

WSGI_APPLICATION = 'meta_id.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt_BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Authentication
AUTH_USER_MODEL = 'authentication.User'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_REDIRECT_URL = '/developer/aplicacoes/'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

ALLOWED_FILES = [
    'application/pdf',
    'application/msword',
    'application/excel',
    'application/x-excel',
    'application/vnd.ms-excel',
    'application/x-msexcel',
    'application/powerpoint',
    'application/mspowerpoint',
    'application/x-mspowerpoint',
    'application/vnd.ms-powerpoint',
    'application/vnd.oasis.opendocument.text',
    'application/vnd.oasis.opendocument.presentation',
    'application/vnd.oasis.opendocument.spreadsheet',
    'application/vnd.sun.xml.writer',
    'application/vnd.sun.xml.writer.global',
    'application/vnd.sun.xml.impress',
    'application/vnd.sun.xml.draw',
    'application/vnd.sun.xml.calc',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.openxmlformats-officedocument.presentationml.slide',
    'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'application/x-7z-compressed',
    'application/zip',
    'application/x-rar-compressed',
    'image/png',
    'image/gif',
    'image/jpg',
    'image/jpeg',
    'image/pjpeg',
    'image/tiff',
    'image/x-tiff',
    'image/bmp',
    'image/x-windows-bmp',
    'audio/ogg',
    'audio/mpeg',
    'audio/mpeg3',
    'audio/mp3',
    'audio/mp4'
    'audio/x-mpeg-3',
    'audio/voc',
    'audio/wav',
    'audio/x-wav',
    'audio/aiff',
    'audio/x-aiff',
    'audio/midi',
    'audio/x-mid',
    'audio/x-midi',
    'audio/webm',
    'application/mp4',
    'application/x-troff-msvideo',
    'application/vnd.rn-realmedia',
    'application/ogg'
    'video/mp4',
    'video/mpeg',
    'video/ogg',
    'video/x-mpeg',
    'video/avi',
    'video/msvideo',
    'video/x-msvideo',
    'video/x-dv',
    'video/quicktime'
    'video/webm',
    'video/H261',
    'video/H263',
    'video/H263-1998',
    'video/H263-2000',
    'video/H264',
    'video/H264-RCDO',
    'video/H264-SVC '
]

# Django Rest Framework
REST_FRAMEWORK = {
    'DATE_FORMAT': "%d/%m/%Y",
    'DATE_INPUT_FORMATS': ["%d/%m/%Y", "%d/%m/%y"],
    'PAGE_SIZE': 100,
    'EXCEPTION_HANDLER': 'meta_id.core.exceptions.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    )
}

# Desabilitando o friendly browser view do Django Rest Framework
if not settings.DEBUG:
    REST_FRAMEWORK.update({
        'DEFAULT_RENDERER_CLASSES': (
            'meta_id.core.renderers.UnicodeJSONRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
        )
    })


# Local configuration
# TODO: Separate in multiple settings
if settings.DEBUG:
    INSTALLED_APPS += (
        'corsheaders',
    )

    MIDDLEWARE_CLASSES = (
        'corsheaders.middleware.CorsMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    CORS_ORIGIN_ALLOW_ALL = os.getenv('DEBUG', False)

    # Define CORS to allow client in development mode
    CORS_ORIGIN_WHITELIST = (
        'localhost:5000',
        'procult.local:5000',
        '0.0.0.0:5000',
    )

    # Model Mommy
    MOMMY_CUSTOM_FIELDS_GEN = {
        'postgres.fields.json_field.JSONField': 'meta_id.test.model_mommy.fields.generate_json_value',
    }

RAVEN_CONFIG = {
    'dsn': os.getenv('RAVEN_DSN_URL'),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(BASE_DIR),
}
