from .common import *

DEBUG = True

# SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'
SECRET_KEY = 'NitT185#'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'NitT185#'
    }
}

CELERY_BROKER_URL = 'redis://default:Rm1cBsFWVui4iEVAeMHd8tnQc148X6QI@redis-11662.c321.us-east-1-2.ec2.redns.redis-cloud.com:11662'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://default:Rm1cBsFWVui4iEVAeMHd8tnQc148X6QI@redis-11662.c321.us-east-1-2.ec2.redns.redis-cloud.com:11662',
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
