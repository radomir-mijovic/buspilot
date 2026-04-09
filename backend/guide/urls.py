from django.urls import path

from .views import (
    GuideCreateView,
    GuideDeleteView,
    GuideEditFormView,
    GuideListView,
    GuideUpdateView,
)

app_name = "guide"


urlpatterns = [
    path(
        "guides",
        GuideListView.as_view(),
        name="guides",
    ),
    path(
        "guides-create",
        GuideCreateView.as_view(),
        name="guides_create",
    ),
    path(
        "guide-update/<int:pk>/",
        GuideUpdateView.as_view(),
        name="guide_update",
    ),
    path(
        "guide-delete/<int:pk>/",
        GuideDeleteView.as_view(),
        name="guide_delete",
    ),
    path(
        "guide-edit-form/<int:pk>/",
        GuideEditFormView.as_view(),
        name="guide_edit_form",
    ),
]
