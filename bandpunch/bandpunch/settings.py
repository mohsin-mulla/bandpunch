"""
Django settings for bandpunch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Add support for dynamic paths
SETTINGS_DIR = os.path.dirname(__file__)

# Define template path and join up the path with the BASE_DIR variable
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

# Define the filename of the database using the BASE_DIR variable to store it in the parent project directory
DATABASE_PATH = os.path.join(BASE_DIR, 'bandpunch.db')

# Define the media path and join up the path with the BASE_DIR variable
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Left side menu processing
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o8%aeuoz+a0x0ze!2mzs5yqe36la)qw7@(=p0kg1_+le%*oum3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'carton',
    'ticket',
    'bootstrap3',
    'widget_tweaks',
    'registration',
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

ROOT_URLCONF = 'bandpunch.urls'

WSGI_APPLICATION = 'bandpunch.wsgi.application'


# This removes the need for an SMTP server for testing purposes, and prints all e-mails to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Django Suit configuration
SUIT_CONFIG = {
    'ADMIN_NAME': 'Bandpunch Administration',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'LIST_PER_PAGE': 20,
}

# Django-Bootstrap3 configuration
BOOTSTRAP3 = {
    'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/',
    'javascript_url': None,
    'include_jquery': True,
    'set_required': True,
}


# Django Registration Redux configuration
REGISTRATION_OPEN = True        # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 1
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/' 
LOGIN_URL = '/accounts/login/'  

# Django Cart configuration
CART_PRODUCT_MODEL = 'ticket.models.Event'