from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from agency.documents.forms import AgencyDocumentUploadForm
from ride.mixins import RidesCountMixin

from .forms import AgencyCreateForm
from .mixins import AgencyQueryFilterMixin
from .models import Agency


class AgencyListView(
    LoginRequiredMixin,
    RidesCountMixin,
    AgencyQueryFilterMixin,
    generic.ListView,
):
    template_name = "agencies.html"
    context_object_name = "agencies"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = AgencyCreateForm
        return context


class AgencyDetailView(
    LoginRequiredMixin,
    RidesCountMixin,
    AgencyQueryFilterMixin,
    generic.DetailView,
):
    template_name = "agency-details.html"
    context_object_name = "agency"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        instance = self.get_object()
        context = super().get_context_data(**kwargs)
        context["form"] = AgencyCreateForm(instance=instance)
        context["document_form"] = AgencyDocumentUploadForm()
        return context


class AgencyCreateView(
    LoginRequiredMixin,
    AgencyQueryFilterMixin,
    generic.CreateView,
):
    form_class = AgencyCreateForm
    model = Agency
    success_url = reverse_lazy("agency:agency_list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.company = self.company
        form.save()
        messages.success(self.request, _("Agency successfully created"))
        return redirect("agency:agency_list")

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect("agency:agency_list")


class AgencyUpdateView(
    LoginRequiredMixin,
    AgencyQueryFilterMixin,
    generic.UpdateView,
):
    form_class = AgencyCreateForm
    model = Agency
    template_name = "agency-update.html"
    success_url = reverse_lazy("agency:agency_list")
    context_object_name = "agency"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(
            self.request,
            _("Agency successfully updated"),
        )
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        agency = self.get_object()
        return redirect("agency:agency_update", pk=agency.pk)

    def get_success_url(self) -> str:
        agency = self.get_object()
        return reverse(
            "agency:agency_details",
            kwargs={"pk": agency.pk},
        )


class AgencyDeleteView(
    LoginRequiredMixin,
    AgencyQueryFilterMixin,
    generic.DeleteView,
):
    model = Agency
    success_url = reverse_lazy("agency:agency_list")

    def get_queryset(self) -> models.QuerySet[Any]:
        return Agency.objects.filter(
            company=self.company,
        )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        agency = self.get_object()
        messages.info(
            self.request,
            _(f"{agency.name} successfully deleted"),
        )
        return super().form_valid(form)
