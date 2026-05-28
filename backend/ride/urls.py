from django.urls import path

from .views import (
    RideConfirmView,
    RideCreateView,
    RideDeleteView,
    RideListView,
    RideUpdateView,
)

app_name = "ride"


urlpatterns = [
    path(
        "rides",
        RideListView.as_view(),
        name="ride_list",
    ),
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
    path(
        "rides-delete/<int:pk>/",
        RideDeleteView.as_view(),
        name="ride_delete",
    ),
    path(
        "rides-confirm/<int:pk>/",
        RideConfirmView.as_view(),
        name="ride_confirm",
    ),
]
