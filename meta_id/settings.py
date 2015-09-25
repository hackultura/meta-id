"""
Django settings for meta-id project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Aviso: Tenta obter uma chave através de uma variavél de ambiente
# Caso não encontre, utiliza uma chave de 49 caracteres gerada automaticamente
# durante a criação do projeto.
SECRET_KEY = os.getenv(
    'META_ID_SECRET_KEY',
    'x@4$z5(ynk6gaza@h+2e&8v_&vy^8wznx#0*f6e+%bwz5rvxzv'
)

# AVISO: Não execute sua aplicação em produção com o DEBUG ligado.
# O padrão é False(Desligado), sendo necessário setar a variável META_ID_DEBUG
# como True para que o DEBUG passe a funcionar.
DEBUG = os.getenv(
    'META_ID_DEBUG',
    False
)

TEMPLATE_DEBUG = os.getenv(
    'META_ID_TEMPLATE_DEBUG',
    False
)

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
    'rest_framework',
    'debug_toolbar',
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
    'default': dj_database_url.config(
        default=os.getenv(
            'META_ID_DATABASE_URL',
            'postgres://meta_id:123456@localhost/meta_id_app'

        )
    )
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
