from django.apps import AppConfig


class DriverConfig(AppConfig):
    name = "driver"

    def ready(self) -> None:
        import driver.signals  # noqa: F401
