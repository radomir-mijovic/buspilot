from django.urls import path

from agency.documents.views import AgencyDocumentDeleteView, AgencyDocumentUploadView

from .views import (
    AgencyCreateView,
    AgencyDeleteView,
    AgencyDetailView,
    AgencyListView,
    AgencyUpdateView,
)

app_name = "agency"

urlpatterns = [
    path(
        "agencies",
        AgencyListView.as_view(),
        name="agency_list",
    ),
    path(
        "agency-details/<int:pk>/",
        AgencyDetailView.as_view(),
        name="agency_details",
    ),
    path(
        "agency-create",
        AgencyCreateView.as_view(),
        name="agency_create",
    ),
    path(
        "agency-update/<int:pk>/",
        AgencyUpdateView.as_view(),
        name="agency_update",
    ),
    path(
        "agency-delete/<int:pk>/",
        AgencyDeleteView.as_view(),
        name="agency_delete",
    ),
    path(
        "agency-documents/<int:agency_pk>/",
        AgencyDocumentUploadView.as_view(),
        name="document_upload",
    ),
    path(
        "agency-document-delete/<int:pk>/<int:agency_pk>/",
        AgencyDocumentDeleteView.as_view(),
        name="document_delete",
    ),
]
