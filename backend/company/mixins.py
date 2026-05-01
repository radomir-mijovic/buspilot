from abc import ABC, abstractmethod
from typing import Any, Type

from django.db import models


class CompanyRequestMixin:
    @property
    def company(self):
        return self.request.user.company


class SetCompanyInKwargsMixin(CompanyRequestMixin):
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["company"] = self.company
        return kwargs


class FilterByCompanyMixin(CompanyRequestMixin, ABC):
    @property
    @abstractmethod
    def filter_model(self) -> Type[models.Model]: ...

    def get_queryset(self):
        return self.filter_model.objects.filter(
            company=self.company,
        )
