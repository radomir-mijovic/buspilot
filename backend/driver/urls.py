from django.urls import path

from .views import DriverCreateView, DriverDeleteView, DriverEditFormView, DriverListView, DriverUpdateView

app_name = "driver"


urlpatterns = [
    path(
        "drivers",
        DriverListView.as_view(),
        name="drivers",
    ),
    path(
        "drivers-create",
        DriverCreateView.as_view(),
        name="drivers_create",
    ),
    path(
        "driver-update/<int:pk>/",
        DriverUpdateView.as_view(),
        name="driver_update",
    ),
    path(
        "driver-delete/<int:pk>/",
        DriverDeleteView.as_view(),
        name="driver_delete",
    ),
    path(
        "driver-edit-form/<int:pk>/",
        DriverEditFormView.as_view(),
        name="driver_edit_form",
    ),
]
