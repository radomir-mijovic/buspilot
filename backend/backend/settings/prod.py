import sentry_sdk

from .base import *  # noqa: F403

DEBUG = False

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),  # noqa: F405
    environment=os.environ.get("SENTRY_ENV", "prod"),  # noqa: F405
    send_default_pii=True,
)

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(  # noqa: F405
    ","
)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DJANGO_VITE = {
    "default": {
        "dev_mode": False,
        "manifest_path": BASE_DIR / "static" / "manifest.json",
    },
}
