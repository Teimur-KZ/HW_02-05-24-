"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = 'django-insecure-^p%e8p+gjj47pw1v@gw)-*x_6m*o5^5(+hdsw+xflb)y+p#6ox' #!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False # режим отладки #!
SESSION_COOKIE_SECURE = True #!
CSRF_COOKIE_SECURE = True #!

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'Teimur.pythonanywhere.com'] # список хостов, которые могут обращаться к проекту


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication_app', # приложения аутентификации
    'cart_app', # приложение корзины
    'customers_app', # приложение покупателей
    'orders_app', # приложение заказов
    'products_app', # приложение продуктов
    'pages_app', # приложение страниц
    'ckeditor', # приложение для визуального редактирования текста

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

ROOT_URLCONF = 'myshop.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # путь к папке с шаблонами
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

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Teimur$default',
        'USER': 'Teimur',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'Teimur.mysql.pythonanywhere-services.com',
        'OPTIONS': {
             'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru' #'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static') # путь к папке со статическими файлами (!!!)
STATIC_ROOT = BASE_DIR / 'static/' # путь к папке со статическими файлами (!!!)

MEDIA_URL = '/media/' # путь к медиафайлам (!!!)
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # путь к папке с медиафайлами (!!!)
MEDIA_ROOT = BASE_DIR / 'media' # путь к папке с медиафайлами (!!!)
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# logging settings:

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'simple': { # simple - простое форматирование
#             'format': '%(levelname)s %(message)s'
#         },
#         'verbose': { # verbose - подробное форматирование
#             'format': '{levelname} {asctime} {module} {process} {thread} {message}',
#             'style': '{',
#             # asctime - время создания записи
#             # module - имя модуля, в котором создана запись
#             # process - идентификатор процесса, создавшего запись
#             # thread - идентификатор потока, создавшего запись
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': './log/django_project.log',
#             'formatter': 'verbose',
#             'encoding': 'utf-8',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': 'INFO',
#         },
#     },
#     'authentications_app': {
#         'handlers': ['console', 'file'],
#         'level': 'DEBUG', # уровень логирования
#         'propagate': True, # пропагация сообщений
#     },
#     'cart_app': {
#         'handlers': ['console', 'file'],
#         'level': 'DEBUG',
#         'propagate': True,
#     },
#     'customers_app': {
#         'handlers': ['console', 'file'],
#         'level': 'DEBUG',
#         'propagate': True,
#     },
#     'orders_app': {
#         'handlers': ['console', 'file'],
#         'level': 'DEBUG',
#         'propagate': True,
#     },
#     'products_app': {
#         'handlers': ['console', 'file'],
#         'level': 'DEBUG',
#         'propagate': True,
#     },
# }



