from rest_framework.routers import DefaultRouter

from .api_views import DriverDetailViewSet

router = DefaultRouter(trailing_slash=True)

app_name = "driver_api"

router.register(r"drivers", DriverDetailViewSet, basename="driver_detail")

urlpatterns = router.urls
