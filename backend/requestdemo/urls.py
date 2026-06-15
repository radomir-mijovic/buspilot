from django.urls import path

from .views import request_demo

app_name = "request_demo"


urlpatterns = [path("request-demo", request_demo, name="request_demo")]
