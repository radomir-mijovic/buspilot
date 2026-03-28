from django.urls import path

from .views import change_password, login_user, logout_user

app_name = "auth"

urlpatterns = [
    path(r"login", login_user, name="login"),
    path(r"logout", logout_user, name="logout"),
    path(r"change-password", change_password, name="change_password"),
]
