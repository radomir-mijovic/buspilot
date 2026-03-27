from django.urls import path

from . import views

app_name = "vehicle"

urlpatterns = [path(r"vehicles", views.VehicleView.as_view(), name="vehicles")]
