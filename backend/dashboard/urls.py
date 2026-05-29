from django.urls import path

from .views import calendar, dashboard

app_name = "dashboard"

urlpatterns = [
    path(
        r"dashboard",
        dashboard,
        name="dashboard",
    ),
    path(
        "calendar",
        calendar,
        name="calendar",
    ),
]
