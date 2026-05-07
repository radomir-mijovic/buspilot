from django.apps import AppConfig


class GuideConfig(AppConfig):
    name = "guide"

    def ready(self) -> None:
        import guide.signals  # noqa: F401
