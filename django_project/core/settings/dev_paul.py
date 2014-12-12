from .dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'wms_client',
        'USER': 'wms_client',
        'PASSWORD': 'OhCi4ohS',
        'HOST': 'localhost',
        'PORT': '',
    }
}