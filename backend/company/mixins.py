from typing import Any


class CompanyRequestMixin:
    @property
    def company(self):
        return self.request.user.company



class SetCompanyInKwargsMixin(CompanyRequestMixin):
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["company"] = self.company
        return kwargs
