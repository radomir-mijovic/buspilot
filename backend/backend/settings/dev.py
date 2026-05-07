from .base import *  # noqa: F403

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [  # noqa: F405
    "django_extensions",
    "debug_toolbar",
]

MIDDLEWARE += [  # noqa: F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG,
}
