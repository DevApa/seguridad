"""
Django settings for seguridad project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+k_yr4$auan5bbo^nog@byt%)x5%a@r()kmf4m9=_w95v6pnli'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'django_freezer',
    'easyaudit',
    'crispy_forms',
    'widget_tweaks',
    'import_export',
]

LOCAL_APPS = [
    'authentication',
    'conf',
    'layout',
    'inventory',
    'organization',
    'documents',
]

INSTALLED_APPS = BASE_APPS + THIRD_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'seguridad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'seguridad.initialize.load_menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'seguridad.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

CONEXION_NAME = 'seguridad'
CONEXION_USER = 'dba'
CONEXION_PASSWORD = 'dba_2022'
CONEXION_HOST = 'localhost'
CONEXION_PORT = 5432

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONEXION_NAME,
        'USER': CONEXION_USER,
        'PASSWORD': CONEXION_PASSWORD,
        'HOST': CONEXION_HOST,
        'PORT': CONEXION_PORT,
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = ('%d/%m/%Y')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

email_send = False
# SMTP Configure
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'academycmav@gmail.com'
EMAIL_HOST_PASSWORD = 'Ap4r1c101982'
DEFAULT_FROM_EMAIL = 'academycmav@gmail.com'

LOGIN_REDIRECT_URL = '/authentication/pages-login'
LOGOUT_REDIRECT_URL = '/authentication/pages-login'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DJANGO_EASY_AUDIT_WATCH_MODEL_EVENTS = True
DJANGO_EASY_AUDIT_WATCH_AUTH_EVENTS = True
DJANGO_EASY_AUDIT_WATCH_REQUEST_EVENTS = True

DJANGO_EASY_AUDIT_ADMIN_SHOW_MODEL_EVENTS = False
DJANGO_EASY_AUDIT_ADMIN_SHOW_AUTH_EVENTS = False
DJANGO_EASY_AUDIT_ADMIN_SHOW_REQUEST_EVENTS = False

AUTH_USER_MODEL = 'authentication.Usuario'
