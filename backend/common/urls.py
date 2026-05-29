from django.urls import path

from .views import expired_documents, expiring_documents, index

app_name = "common"


urlpatterns = [
    path(
        "",
        index,
        name="index",
    ),
    path(
        "expiring-documents",
        expiring_documents,
        name="expiring_documents",
    ),
    path(
        "expired-documents",
        expired_documents,
        name="expired_documents",
    ),
]
