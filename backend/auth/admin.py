from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["id", "username", "company"]
    list_filter = ["company"]
    search_fields = ["username", "company__name"]

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Company Info", {"fields": ("company",)}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Company Info", {"fields": ("company",)}),
    )
