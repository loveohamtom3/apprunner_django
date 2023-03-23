import os

from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0=limiw24v7#rnr(cf!3p0akvgz0)lgw0$_ri5%))rim=+!g1q'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql_testdb',
        'USER': 'newuser',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '3306',
    }
}

ALLOWED_HOSTS           = [ "xakezxsmjn.ap-northeast-1.awsapprunner.com" ]
CSRF_TRUSTED_ORIGINS    = [ "https://xakezxsmjn.ap-northeast-1.awsapprunner.com" ]
