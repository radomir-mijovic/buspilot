from django.urls import path

from .views import (
    DefectCreateView,
    DefectDeleteView,
    DefectListView,
    DefectMarkAsResolved,
)

app_name = "defect"


urlpatterns = [
    path(
        "defects",
        DefectListView.as_view(),
        name="defects",
    ),
    path(
        "defect-create",
        DefectCreateView.as_view(),
        name="defect_create",
    ),
    path(
        "mark-as-resolved/<int:pk>/",
        DefectMarkAsResolved.as_view(),
        name="mark_as_resolved",
    ),
    path(
        "defect-delete/<int:pk>/",
        DefectDeleteView.as_view(),
        name="defect_delete",
    ),
]
