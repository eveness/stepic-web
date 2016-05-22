import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'h8t1l_&lm*aae$!!^198!qs1&i1uauz=zj(a1mvr9_#*#^r9b)'
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = []

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'ask.urls'

WSGI_APPLICATION = 'ask.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'