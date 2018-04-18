"""
Django settings for serenity project.

Generated by 'django-admin startproject' using Django 1.11b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=if7ygheesanfsy*t1vt7c^2sd#f7fn-&&^s89dgz%v6x-6!$!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'dougcoleman.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clients.apps.ClientsConfig',
    'neighborhoodwatch.apps.NeighborhoodwatchConfig',
    'calllog.apps.CalllogConfig',
    'shelter.apps.ShelterConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'serenity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./serenity/templates',],
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

#TEMPLATE_LOADERS: 'django.template.loaders.filesystem.Loader'

WSGI_APPLICATION = 'serenity.wsgi.application'

# Session
# https://docs.djangoproject.com/en/1.11/topics/http/sessions/

#TIME = 5*60
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_COOKIE_HTTPONLY = True
#SESSION_COOKIE_AGE = TIME
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_IDLE_TIME = TIME



# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dougcoleman$serenity',
        'HOST': 'dougcoleman.mysql.pythonanywhere-services.com',
        'USERNAME': 'dougcoleman',
        'PASSWORD': 'fr@nklin2121'
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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

# Security stuff
# https://docs.djangoproject.com/en/2.0/topics/security/

#SECURE_PROXY_SSL_HEADER = True
SECURE_SSL_REDIRECT = True
#SECURE_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_HSTS_SECONDS = True
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

DATE_INPUT_FORMATS = ['%d-%m-%Y']

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = u'/home/dougcoleman/serenity/media'
MEDIA_URL = '/media/'
STATIC_ROOT = u'/home/dougcoleman/serenity/static'
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'