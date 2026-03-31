from django.urls import path

from . import views
from .documents.views import VehicleDocumentDeleteView, VehicleDocumentUploadView

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
    path(
        "vehicle-documents/<int:vehicle_pk>/",
        VehicleDocumentUploadView.as_view(),
        name="document_upload",
    ),
    path(
        "vehicle-documents-delete/<int:pk>/",
        VehicleDocumentDeleteView.as_view(),
        name="document_delete",
    ),
]
