from typing import Type

from django.db import models

from company.mixins import FilterByCompanyMixin
from vehicle.models import Vehicle


class VehicleQueryFilterMixin(FilterByCompanyMixin):
    @property
    def filter_model(self) -> Type[models.Model]:
        return Vehicle

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("company")
