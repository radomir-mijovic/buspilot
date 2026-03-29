from django.urls import path

from . import views

app_name = "vehicle"

urlpatterns = [
    path(
        "vehicles",
        views.VehicleView.as_view(),
        name="vehicles",
    ),
    path(
        "vehicles/<int:pk>/",
        views.VehicleDetailView.as_view(),
        name="vehicles_details",
    ),
    path(
        "vehicles-create",
        views.VehicleCreateView.as_view(),
        name="vehicles_create",
    ),
    path(
        "vehicles-update/<int:pk>/",
        views.VehicleUpdateView.as_view(),
        name="vehicles_update",
    ),
    path(
        "vehicles-delete/<int:pk>/",
        views.VehicleDeleteView.as_view(),
        name="vehicles_delete",
    ),
]
