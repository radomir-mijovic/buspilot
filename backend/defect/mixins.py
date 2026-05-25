from typing import Type

from django.db import models

from company.mixins import FilterByCompanyMixin
from .models import Defect


class DefectQueryFilterMixin(FilterByCompanyMixin):
    @property
    def filter_model(self) -> Type[models.Model]:
        return Defect

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("vehicle", "reported_by")
