from rest_framework.routers import DefaultRouter

from .api_views import DriverDetailViewSet, DriverPortalViewSet

router = DefaultRouter(trailing_slash=True)

app_name = "driver_api"

router.register(r"drivers", DriverDetailViewSet, basename="driver_detail")
router.register(r"driver-portal", DriverPortalViewSet, basename="driver_portal")

urlpatterns = router.urls
