from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("agency.urls")),
    path("", include("auth.urls")),
    path("", include("dashboard.urls")),
    path("", include("driver.urls")),
    path("", include("guide.urls")),
    path("", include("vehicle.urls")),
    path("", include("ride.urls")),
    path("", include("common.urls")),
    path("api/", include("ride.api.urls")),
    path("api/", include("vehicle.api.urls")),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
