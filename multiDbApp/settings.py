# @Date:   2017-05-20T19:44:16+05:30
# @Last modified time: 2017-05-21T12:15:24+05:30



"""
Django settings for multiDbApp project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6b!p7)t%t+xn@@r%9jdkf*x#f-+!dphuwz-)k3!7bome89*e%p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.WhichDatabaseIsTOUseMIddleware'
]

ROOT_URLCONF = 'multiDbApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'multiDbApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdbdefault',
        'USER':"root",
        'PASSWORD':"root",
        'PORT':'3306'
    },
    'testdb1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb1',
        'USER':"root",
        'PASSWORD':"root",
        'PORT':'3306'
    },
    'testdb2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb2',
        'USER':"root",
        'PASSWORD':"root",
        'PORT':'3306'
    },
    'testdb3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb3',
        'USER':"root",
        'PASSWORD':"root",
        'PORT':'3306'
    },
    'testdb4': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb4',
        'USER':"root",
        'PASSWORD':"root",
        'PORT':'3306'
    },
    'testdb5': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb5',
        'USER':"root",
        'PASSWORD':"root",
        'PORT':'3306'
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
