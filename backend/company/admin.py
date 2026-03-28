from django.contrib import admin

from .models import Company, CompanyAddress


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]



@admin.register(CompanyAddress)
class CompanyAddressAdmin(admin.ModelAdmin):
    list_display = ["id", "company"]
