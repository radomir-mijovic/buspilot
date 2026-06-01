from django.urls import path

from .api_views import ChangePasswordView

app_name = "auth_api"

urlpatterns = [
    path(
        "change-password",
        ChangePasswordView.as_view(),
        name="change_password",
    )
]
