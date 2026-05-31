from rest_framework.routers import DefaultRouter

from .api_views import ExpiringDocumentsViewSet

app_name = "driver_documents_api"

router = DefaultRouter(trailing_slash=True)

router.register(
    r"expiring-documents",
    ExpiringDocumentsViewSet,
    basename="expiring_documents",
)

urlpatterns = router.urls
