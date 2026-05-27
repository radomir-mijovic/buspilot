from typing import Any, Type
from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.db.models import Q
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import generic

from auth.decorators import admin_permission_required
from company.mixins import DocumentsQuerySetMixin, FilterByCompanyMixin
from company.models import CompanyDocument

from .forms import CompanyDocumentUploadForm


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class CompanyDocumentView(
    LoginRequiredMixin,
    FilterByCompanyMixin,
    DocumentsQuerySetMixin,
    generic.CreateView,
    generic.ListView,
):
    context_object_name = "documents"
    form_class = CompanyDocumentUploadForm
    model = CompanyDocument
    paginate_by = 10
    template_name = "../templates/company-documents.html"

    @property
    def filter_model(self) -> Type[models.Model]:
        return CompanyDocument

    def form_valid(self, form):
        form.instance.company = self.company
        form.save()
        messages.success(self.request, _("File successfully added."))
        return redirect("company:company_documents")

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        for error in form.errors.values():
            messages.error(self.request, error.as_text())
        return redirect("company:company_documents")

    def get_queryset(self):
        owner = self.request.GET.get("owner", "")
        search_param = self.request.GET.get("search_param", "")

        if "driver" in owner:
            qs = self.get_drivers_documents()

        elif "agency" in owner:
            qs = self.get_agency_documents()

        elif "vehicle" in owner:
            qs = self.get_vehicles_documents()

        else:
            qs = super().get_queryset()

        if search_param:
            qs = self.filter_queryset(search_param, qs)

        return qs

    def filter_queryset(self, value: str, qs: models.QuerySet[Any]):
        return qs.filter(
            Q(title__icontains=value) | Q(document_type__icontains=value),
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        owner = self.request.GET.get("owner", "")
        search_param = self.request.GET.get("search_param", "")
        context = super().get_context_data(**kwargs)
        context["document_form"] = CompanyDocumentUploadForm()
        context["owner"] = owner
        context["search_param"] = search_param
        return context


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class CompanyDocumentDeleteView(
    DocumentsQuerySetMixin,
    LoginRequiredMixin,
    generic.DeleteView,
):
    model = CompanyDocument
    success_url = reverse_lazy("company:company_documents")

    def get_queryset(self) -> models.QuerySet[Any]:
        owner = self.request.GET.get("owner", "")

        if "driver" in owner:
            qs = self.get_drivers_documents()

        elif "agency" in owner:
            qs = self.get_agency_documents()

        elif "vehicle" in owner:
            qs = self.get_vehicles_documents()

        else:
            qs = CompanyDocument.objects.filter(
                company=self.company,
            )

        return qs

    def get(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse:
        return self.delete(request, *args, **kwargs)

    def get_success_url(self) -> str:
        owner = self.request.GET.get("owner", "")
        return f"{reverse('company:company_documents')}?{urlencode({'owner': owner})}"
