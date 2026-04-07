from django.urls import path

from .views import RideCreateView, RideUpdateView

app_name = "ride"


urlpatterns = [
    path(
        "rides-create",
        RideCreateView.as_view(),
        name="ride_create",
    ),
    path(
        "rides-update/<int:pk>/",
        RideUpdateView.as_view(),
        name="ride_update",
    ),
]
