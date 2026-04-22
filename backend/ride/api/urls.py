from rest_framework.routers import DefaultRouter

from .api_views import (
    RideViewSet
)

app_name = "ride_api"

router = DefaultRouter(trailing_slash=True)

router.register(r"rides", RideViewSet, basename="ride")

urlpatterns = router.urls
