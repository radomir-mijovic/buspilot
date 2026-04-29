from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from company.mixins import CompanyRequestMixin
from driver.models import Driver, DriverDocument

from .forms import DriverDocumentUploadForm


class DriverDocumentUploadView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.CreateView,
):
    model = DriverDocument
    form_class = DriverDocumentUploadForm
    template_name = "../templates/driver-details.html"

    def form_valid(self, form):
        form.instance.driver = self.driver
        form.instance.company = self.company
        form.save()
        messages.success(self.request, "File successfully added.")
        return redirect("driver:driver_details", pk=self.driver_pk)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        for error in form.errors.values():
            messages.error(self.request, error.as_text())
        return redirect("driver:driver_details", pk=self.driver_pk)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["driver"] = self.driver
        context["document_form"] = DriverDocumentUploadForm()
        return context

    @property
    def driver_pk(self) -> int | None:
        return self.kwargs.get("driver_pk")

    @property
    def driver(self):
        return get_object_or_404(Driver, pk=self.driver_pk)


class DriverDocumentDeleteView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.DeleteView,
):
    model = DriverDocument
    success_url = reverse_lazy("driver:drivers")

    def get_queryset(self) -> models.QuerySet[Any]:
        return DriverDocument.objects.filter(
            driver__company=self.company,
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
            "driver:driver_details",
            kwargs={"pk": self.driver_pk},
        )

    @property
    def driver_pk(self) -> int | None:
        return self.kwargs.get("driver_pk")
