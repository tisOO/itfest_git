"""
Django settings for itfest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%q%xtpslya6lx(zpix@1uolwy4f^1c%l)8f6+c&2v=ck*&*70q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


TEMPLATE_CONTEXT_PROCCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.contrib.staticfiles',
	#'itfest.main.context_processors.itfest_proc',
)


TEMPLATE_DIRS = (
	'D:/works/python_projects/dj_projects/itfest_git/itfest/templates',
	'D:/works/python_projects/dj_projects/itfest_git/itfest/templates/project',
)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	#'django.contrib.staticfiles.finders.FileSystemFinder',
	#'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'itfest.tasks',
    'itfest.users',
    'itfest.task_table',
    'itfest.info',
	'itfest.main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'itfest.urls'

WSGI_APPLICATION = 'itfest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'itfest',
	'USER': 'root', 
	'PASSWORD': '',
	'HOST': '127.0.0.1', 
	'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'D:/works/python_projects/dj_projects/itfest_git/itfest/templates/static'
STATICFILES_DIRS = (
	'D:/works/python_projects/dj_projects/itfest_git/itfest/templates/project',
)

#MEDIA_ROOT = 'D:/works/python_projects/dj_projects/itfest_git/itfest/templates/project'