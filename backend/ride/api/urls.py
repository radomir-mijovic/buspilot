from rest_framework.routers import DefaultRouter

from .api_views import RideCreateViewSet, RideUpdateViewSet, RideRetrieveViewSet

app_name = "ride_api"

router = DefaultRouter(trailing_slash=True)

router.register(r"rides", RideRetrieveViewSet, basename="ride_retrieve")
router.register(r"rides", RideCreateViewSet, basename="ride_create")
router.register(r"rides-update", RideUpdateViewSet, basename="ride_update")

urlpatterns = router.urls
