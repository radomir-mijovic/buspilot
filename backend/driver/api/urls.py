from rest_framework.routers import DefaultRouter

from .api_views import DriverDetailViewSet, DriverRidesViewSet

router = DefaultRouter(trailing_slash=True)

app_name = "driver_api"

router.register(r"drivers", DriverDetailViewSet, basename="driver_detail")
router.register(r"driver-rides", DriverRidesViewSet, basename="driver_rides")

urlpatterns = router.urls
