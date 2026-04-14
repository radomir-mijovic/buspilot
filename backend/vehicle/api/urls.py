from rest_framework.routers import DefaultRouter

from .api_views import VehicleDetailViewSet

router = DefaultRouter(trailing_slash=True)

app_name = "vehicle_api"

router.register(r"vehicles", VehicleDetailViewSet, basename="vehicle_detail")

urlpatterns = router.urls
