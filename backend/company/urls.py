from django.urls import path

from company.documents.views import CompanyDocumentDeleteView, CompanyDocumentView

app_name = "company"

urlpatterns = [
    path(
        "company-documents",
        CompanyDocumentView.as_view(),
        name="company_documents",
    ),
    path(
        "document-delete/<int:pk>/",
        CompanyDocumentDeleteView.as_view(),
        name="document_delete",
    ),
]
