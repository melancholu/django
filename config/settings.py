from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env()

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
APPS_DIR = ROOT_DIR / "apps"

DEBUG = env.bool("DJANGO_DEBUG", False)
SECRET_KEY = env("DJANGO_SECRET_KEY")

TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_L10N = True
USE_TZ = True

ALLOWED_HOSTS = ["*"]

DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


DJANGO_APPS = [
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "actstream",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "django_extensions",
    "dj_rest_auth.registration",
]


LOCAL_APPS = [
    "apps.users.apps.UsersConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

STATIC_URL = "/static/"
ROOT_URLCONF = "config.urls"

ADMINS = [("""Safu Ventures Inc.""", "develop@safuventures.com")]
MANAGERS = ADMINS


# dj-rest-auth: https://dj-rest-auth.readthedocs.io/en/latest/index.html
REST_USE_JWT = True
JWT_AUTH_COOKIE = "Bearer"
SIMPLE_JWT = {
    # https://blog.ull.im/engineering/2019/02/07/jwt-strategy.html
    # 주로 access_token: 30min, refresh_token: 2 weeks ~ 1 month
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),  # Firebase allows only max=1h
    "REFRESH_TOKEN_LIFETIME": timedelta(weeks=4),
    "ROTATE_REFRESH_TOKENS": True,
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "apps.users.serializers.RegisterSerializer",
}

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False


AUTH_USER_MODEL = "users.User"

# django-allauth
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True


MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]
