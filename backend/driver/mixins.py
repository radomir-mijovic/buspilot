from typing import Type

from django.db import models

from company.mixins import FilterByCompanyMixin
from driver.models import Driver


class DriverQueryFilterMixin(FilterByCompanyMixin):
    @property
    def filter_model(self) -> Type[models.Model]:
        return Driver
