from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from agency.models import Agency, AgencyDocument
from company.mixins import CompanyRequestMixin

from .forms import AgencyDocumentUploadForm


class AgencyDocumentUploadView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.CreateView,
):
    model = AgencyDocument
    form_class = AgencyDocumentUploadForm
    template_name = "../templates/agency-details.html"

    def form_valid(self, form):
        form.instance.agency = self.agency
        form.instance.company = self.company
        form.save()
        messages.success(self.request, _("File successfully added."))
        return redirect("agency:agency_details", pk=self.agency_pk)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        for error in form.errors.values():
            messages.error(self.request, error.as_text())
        return redirect("agency:agency_details", pk=self.agency_pk)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["agency"] = self.agency
        context["document_form"] = AgencyDocumentUploadForm()
        return context

    @property
    def agency_pk(self) -> int | None:
        return self.kwargs.get("agency_pk")

    @property
    def agency(self):
        return get_object_or_404(Agency, pk=self.agency_pk)


class AgencyDocumentDeleteView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.DeleteView,
):
    model = AgencyDocument
    success_url = reverse_lazy("agency:agencys")

    def get_queryset(self) -> models.QuerySet[Any]:
        return AgencyDocument.objects.filter(
            agency__company=self.company,
        )

    def get(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse:
        return self.delete(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse(
            "agency:agency_details",
            kwargs={"pk": self.agency_pk},
        )

    @property
    def agency_pk(self) -> int | None:
        return self.kwargs.get("agency_pk")
