from django.urls import path

from .views import AgencyCreateView, AgencyListView, AgencyUpdateView

app_name = "agency"

urlpatterns = [
    path(
        "agencies",
        AgencyListView.as_view(),
        name="agency_list",
    ),
    path(
        "agency-create",
        AgencyCreateView.as_view(),
        name="agency_create",
    ),
    path(
        "agency-update/<int:pk>/",
        AgencyUpdateView.as_view(),
        name="agency_update",
    ),
]
