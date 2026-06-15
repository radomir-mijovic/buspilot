from django.urls import path

from .api_views import RequestDemoApiView

app_name = "request_demo_api"


urlpatterns = [path("request-demo", RequestDemoApiView.as_view(), name="request_demo")]
