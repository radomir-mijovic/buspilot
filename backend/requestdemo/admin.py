from django.contrib import admin

from .models import RequestDemo


@admin.register(RequestDemo)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "company"]
