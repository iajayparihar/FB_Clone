from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'FB_Clone',      
        'USER': 'postgres',
        'PASSWORD': '12345', 
        # 'HOST': 'db',
        'HOST': 'localhost',
        'PORT': '5432', 
    }
}