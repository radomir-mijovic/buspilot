from typing import Type

from django.db import models

from agency.models import Agency
from company.mixins import FilterByCompanyMixin


class AgencyQueryFilterMixin(FilterByCompanyMixin):
    @property
    def filter_model(self) -> Type[models.Model]:
        return Agency
