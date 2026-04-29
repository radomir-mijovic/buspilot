from django.urls import path

from .views import expired_documents

app_name = "common"


urlpatterns = [
    path(
        "expiring-documents",
        expired_documents,
        name="expiring_documents",
    )
]
