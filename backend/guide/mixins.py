from typing import Type

from django.db import models

from company.mixins import FilterByCompanyMixin
from guide.models import Guide


class GuideQueryFilterMixin(FilterByCompanyMixin):
    @property
    def filter_model(self) -> Type[models.Model]:
        return Guide
