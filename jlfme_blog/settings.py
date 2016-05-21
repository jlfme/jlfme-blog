#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2016-03-21 20:06:18
# ---------------------------------------


import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vie+ehwq)_6sr1=4ewj5s)m-7-%n!gjxm3ltk6ce%7k8g9zg=o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'tinymce'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'jlfme_blog.urls'

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

WSGI_APPLICATION = 'jlfme_blog.wsgi.application'


# Database
DATABASES = {
    'default': {
        # 'ENGINE': 'mysql.connector.django',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jlfme_blog',
        'USER': 'root',
        'PASSWORD': 'password123',
        'HOST': '10.10.10.4',
        'PORT': '3306',
    }
}


# Password validation
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = False
USE_TZ = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# media upload path
MEDIA_ROOT = 'media/'


# TINYMCE

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    # 'theme_advanced_buttons1':'bold,italic,underline,|,bullist,numlist,outdent,indent,|,undo,redo,|,link,unlink',
    'plugins':'paste,autolink,save,table,preview',
    # 'relative_urls': False,
}
# TINYMCE_SPELLCHECKER = False
# TINYMCE_SPELLCHECKER = False
# TINYMCE_COMPRESSOR = False
# TINYMCE_FILEBROWSER = False
