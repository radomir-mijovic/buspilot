from django.urls import path

from .views import expired_documents, expiring_documents

app_name = "common"


urlpatterns = [
    path(
        "expiring-documents",
        expiring_documents,
        name="expiring_documents",
    ),
    path(
        "expired-documents",
        expired_documents,
        name="expired_documents",
    )
]
