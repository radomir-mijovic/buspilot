from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from company.mixins import CompanyRequestMixin
from ride.mixins import RidesCountMixin

from .forms import AgencyCreateForm
from .models import Agency


class AgencyListView(
    LoginRequiredMixin,
    RidesCountMixin,
    CompanyRequestMixin,
    generic.ListView,
):
    template_name = "agencies.html"
    context_object_name = "agencies"

    def get_queryset(self) -> models.QuerySet[Any]:
        return Agency.objects.filter(company=self.company)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = AgencyCreateForm
        return context


class AgencyCreateView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.CreateView,
):
    form_class = AgencyCreateForm
    model = Agency
    success_url = reverse_lazy("agency:agency_list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.company = self.company
        form.save()
        return redirect("agency:agency_list")

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect("agency:agency_list")


class AgencyUpdateView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.UpdateView,
):
    form_class = AgencyCreateForm
    model = Agency
    template_name = "agency-update.html"
    success_url = reverse_lazy("agency:agency_list")
    context_object_name = "agency"

    def get_queryset(self) -> models.QuerySet[Any]:
        return Agency.objects.filter(
            company=self.company,
        )

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        agency = self.get_object()
        return redirect("agency:agency_update", pk=agency.pk)


class AgencyDeleteView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.DeleteView,
):
    model = Agency
    success_url = reverse_lazy("agency:agency_list")

    def get_queryset(self) -> models.QuerySet[Any]:
        return Agency.objects.filter(
            company=self.company,
        )
