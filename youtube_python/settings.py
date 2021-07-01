
from pathlib import Path
import os
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jt$_mjj&(+!et*kypu-^(9pt@xc+(_55fw4n=*@$kgmu$c1got'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'youtube',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "verify_email.apps.VerifyEmailConfig",
    'crispy_forms',
    'debug_toolbar',
    
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'youtube_python.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['youtube_python/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'youtube_python.wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ==================email verificaation setting ================
def verified_callback(user):
    user.is_active = True


EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_FROM_ADDRESS = 'noreply@aliasaddress.com'
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'email_verify/mail_body.html'
EMAIL_MAIL_PLAIN = 'email_verify/mail_body.txt'
EMAIL_TOKEN_LIFE = 60 * 60
EMAIL_PAGE_TEMPLATE = 'email_verify/confirm.html'
EMAIL_PAGE_DOMAIN = 'http://127.0.0.1:8000/'

# For Django Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sunilsoni10220001022000@gmail.com'
EMAIL_HOST_PASSWORD = 'Sunil1022000'  # os.environ['password_key'] suggested
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'




STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'static/')
MEDIA_URL= "/media/"
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')











django_heroku.settings(locals())