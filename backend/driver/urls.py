from django.urls import path

from driver.documents.views import DriverDocumentDeleteView, DriverDocumentUploadView

from .views import (
    DriverCreateView,
    DriverDeleteView,
    DriverDetailView,
    DriverListView,
    DriverUpdateView,
)

app_name = "driver"


urlpatterns = [
    path(
        "drivers",
        DriverListView.as_view(),
        name="drivers",
    ),
    path(
        "driver-details/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver_details",
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
        "driver-documents/<int:driver_pk>/",
        DriverDocumentUploadView.as_view(),
        name="document_upload",
    ),
    path(
        "driver-document-delete/<int:pk>/<int:driver_pk>/",
        DriverDocumentDeleteView.as_view(),
        name="document_delete",
    ),
]
