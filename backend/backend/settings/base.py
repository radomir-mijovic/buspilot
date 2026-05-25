import os
from pathlib import Path

import sentry_sdk
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

USE_L10N = False
DATE_FORMAT = "d/m/Y"
DATETIME_FORMAT = "d/m/Y H:i"
SHORT_DATE_FORMAT = "d/m/Y"
DATE_INPUT_FORMATS = ["%d/%m/%Y", "%Y-%m-%d"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_countries",
    "rest_framework",
]


LOCAL_APPS = [
    "auth.apps.UserAuthConfig",
    "agency.apps.AgencyConfig",
    "common.apps.CommonConfig",
    "company.apps.CompanyConfig",
    "dashboard.apps.DashboardConfig",
    "defect.apps.DefectConfig",
    "guide.apps.GuideConfig",
    "driver.apps.DriverConfig",
    "ride.apps.RideConfig",
    "vehicle.apps.VehicleConfig",
]


INSTALLED_APPS += LOCAL_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "auth.context_processors.change_password_form",
                "common.context_processors.count_all_in_danger_documents",
                "common.context_processors.list_in_danger_driver_documents",
                "common.context_processors.list_in_danger_vehicle_documents",
                "common.context_processors.list_all_driver_expired_documents",
                "common.context_processors.list_all_vehicle_expired_documents",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

if os.environ.get("DATABASE_ENGINE") == "django.db.backends.postgresql_psycopg2":
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get(
                "DATABASE_ENGINE",
                "django.db.backends.postgresql",
            ),
            "NAME": os.environ.get("DATABASE_NAME", "postgres"),
            "HOST": os.environ.get("DATABASE_HOST", "localhost"),
            "PORT": os.environ.get("DATABASE_PORT", "5432"),
            "USER": os.environ.get("DATABASE_USER", "postgres"),
            "PASSWORD": os.environ.get("DATABASE_PASSWORD", "postgres"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "db.buspilot",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"
LANGUAGES = [
    ("en", _("English")),
    ("me", _("Montenegrin")),
]

TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

LOGIN_URL = "auth:login"


AUTH_USER_MODEL = "user_auth.User"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

# Translation
LOCALE_PATHS = [BASE_DIR / "locale"]

# Sentry
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    environment=os.environ.get("SENTRY_ENV", "dev"),
    send_default_pii=True,
)
