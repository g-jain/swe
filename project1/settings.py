"""
Django settings for project1 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '292+!j3n*-v1e(i)jz-24&g=yauu7%ml2r35p%h%h(+dc9w9l='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
#    'django.contrib.sites',
	'lawyered',
	'bootstrap3',
	'django_markdown',
	'rest_framework',
)

#SITE_ID = 1

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
#    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'project1.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
#                'pybb.context_processors.processor',
			],
		},
	},
]

WSGI_APPLICATION = 'project1.wsgi.application'

#if ON_HEROKU :
#DATABASES = {'default': dj_database_url.config()}
#else:
DATABASES = {
 	'default': {
 		'ENGINE': 'django.db.backends.postgresql_psycopg2',
 		'NAME': 'lawyered',
 		'USER': 'postgres',
 		'PASSWORD': 'hans',
 		'HOST': 'localhost',
 		'PORT': '',
 		#'ENGINE': 'django.db.backends.sqlite3',
 		#'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 	}
}

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
#     'default': {
#       'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'lawyered',
#         'USER': 'swe',
#         'PASSWORD': 'swe',
#         'HOST': 'localhost',
#         'PORT': '',
#         #'ENGINE': 'django.db.backends.sqlite3',
#         #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
	]
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#redirection
LOGIN_REDIRECT_URL = 'lawyered/dashboard'


MEDIA_URL = '/home/project1/lawyered/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# DJANGO_SETTINGS_MODULE  website.settings
