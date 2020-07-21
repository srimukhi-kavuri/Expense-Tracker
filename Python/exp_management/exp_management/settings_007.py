"""
Django settings for botx project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import json
import pymongo









'''

db_base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_base_path_json = os.path.join(db_base_dir, "FAQ",'nlp_engine')


with open(os.path.join(db_base_path_json,  "config_file.json"), "r") as fp:
            config_data_file = json.load(fp)


mongo_conn = pymongo.MongoClient()
db_conn = mongo_conn[config_data_file["data_base"]]








config_data = db_conn["project_configuration"].find({}).count()


if not config_data:
    db_conn["project_configuration"].insert(config_data_file)
    print("=============================dddddd===========================================")


else:
    config_data = db_conn["project_configuration"].find({})[0]
    

db_bot =  config_data["data_base"]

'''




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'otr@xkkjq*5$k3xf-9x_3x%kqt90ye8-7_ww$+e@n1&)ux7zor'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS =["939e981c.ngrok.io",'127.0.0.1','0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_mongoengine',
    'rest_framework',
    'corsheaders',
    'FAQ',
    'feed',
    'display_name',
    'exusers',
    'interview',
    # 'liveAgent',

]
AUTH_USER_MODEL = 'exusers.MyUser'

CORS_ORIGIN_WHITELIST = (
 'google.com',
 'ec2-3-16-154-211.us-east-2.compute.amazonaws.com:9000/',
 'http://ec2-3-16-154-211.us-east-2.compute.amazonaws.com:9000/',
 '3.16.154.211:9000/',
 '127.0.0.1:9000',
 '*',
 'http://3.16.122.10:8019',
 '3.16.122.10:8019',
 'http://ec2-3-16-122-10.us-east-2.compute.amazonaws.com:8019/',
 'ec2-3-16-122-10.us-east-2.compute.amazonaws.com:8019/',
 'localhost:3000',
 'localhost:8080',
 'http://3.16.122.10:8011',
 'http://3.16.122.10:8019',
 '3.16.122.10:8019',
 '3.16.122.10:8011',
 'localhost:3001',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8011',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8012',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8019',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8015',
 'http://ec2-3-16-122-10.us-east-2.compute.amazonaws.com:8011/',
 'ec2-3-16-122-10.us-east-2.compute.amazonaws.com:8011/',
 'http://kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8080',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8080',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8011',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8012',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8015',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8019',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8080',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8007',
 '00d858d9.ngrok.io',
 'https://00d858d9.ngrok.io/',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8011',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:9000',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8011',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8012',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8015',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8019',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8080',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8011',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:9000')

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'FAQ.middleware.SessionRedis',
    # 'FAQ.middleware.SessionIdleTimeout',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
    # 'FAQ_templates.middleware.AutoLogout',
]
# AUTO_LOGOUT_DELAY =1

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
###################### session time ###########
TIME = 60*30  #//four hours  or your time
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = TIME   # //change expired session

SESSION_IDLE_TIMEOUT = TIME  #//logout
##############################################
SESSION_EXPIRE_SECONDS = TIME
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
ROOT_URLCONF = 'botx.urls'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'botx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
MONGOADMIN_OVERRIDE_ADMIN = True
import mongoengine
from urllib.parse import  quote_plus
_MONGODB_USER = quote_plus('nell')
_MONGODB_PASSWD = quote_plus('nell@123')
_MONGODB_HOST = 'localhost'
_MONGODB_PORT = '27017'
_MONGODB_NAME = db_bot
#-------------------------------------------------------------------------#
#                   mongo db Global Settings
#-------------------------------------------------------------------------#
_MONGODB_DATABASE_HOST = \
    'mongodb://%s:%s@%s:%s/%s' \
    % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_PORT, _MONGODB_NAME)

# connect(host='mongodb://superadmin:abceodke42n3@localhost:27017/topazpanel')
mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': db_bot,
       }
   }
# DATABASES = {
#    'default': {
#         'ENGINE': 'django_mongodb_engine',
#         'NAME': 'bot',
#         'USER': 'ritesh',
#         'PASSWORD': 'shree@123',
#         'HOST': 'localhost',
#         'PORT': '27017',
#         'SUPPORTS_TRANSACTIONS': False,
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


##############################email conf####################
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='nell.paresh@gmail.com'
EMAIL_HOST_PASSWORD ='Test@123'

# EMAIL_HOST ='smtp.gmail.com'
# EMAIL_HOST_USER ='nell.paresh@gmail.com'
# EMAIL_HOST_PASSWORD = 'Test@123'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "Media")
MEDIA_URL = "/Media/"
LOGIN_REDIRECT_URL = 'index'
# LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/'
# LOGIN_REDIRECT_URL='/login/'
