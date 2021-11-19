import os

from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('BASE_PORT'),
        'NAME': os.getenv('BASE_NAME'),
        'USER': os.getenv('BASE_USER'),
        'PASSWORD': os.getenv('BASE_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = env.bool('DEBUG_ON_OFF', False)
#DEBUG = False

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('TRUSTED_HOSTS')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
