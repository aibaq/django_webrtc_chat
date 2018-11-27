import os

from configurations import Configuration


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'django_webrtc_chat')


class BaseConfiguration(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = 'qphl#testme&jjbraqxe63%k=)#+q^5*=5ixl$wh82#('

    DEBUG = True

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = [
        'channels',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.postgres',
        'django_webrtc_chat.core',
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

    ROOT_URLCONF = 'django_webrtc_chat.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(PROJECT_DIR, 'templates'), ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django_webrtc_chat.core.context_processors.site_url',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'django_webrtc_chat.wsgi.application'
    ASGI_APPLICATION = 'django_webrtc_chat.routing.application'
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                'hosts': [('127.0.0.1', 6379)],
            },
        },
    }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/static/'
    # STATIC_ROOT = '/static'
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'),)

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

    SITE_URL = 'http://localhost:8000'

    ADMINS = (
    )

    APPEND_SLASH = True


class Dev(BaseConfiguration):
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    SITE_URL = 'https://webrtc.com'
    STATIC_ROOT = '/django_webrtc_chat/static'
    MEDIA_ROOT = '/django_webrtc_chat/media'
