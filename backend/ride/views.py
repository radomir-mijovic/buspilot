from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import RideForm
from .mixins import RidesCountMixin
from .models import Ride


class RideListView(LoginRequiredMixin, RidesCountMixin, generic.ListView):
    template_name = "all-rides.html"
    model = Ride
    context_object_name = "rides"

    def get_queryset(self) -> models.query.QuerySet[Any]:
        return Ride.rides.from_today_and_on().filter(
            company=self.request.user.company,
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        company = self.request.user.company

        context["count_all"] = self.count_all(company)
        context["transfers_count"] = self.transfers_count(company)
        context["excursions_count"] = self.excursions_count(company)
        context["lines_count"] = self.lines_count(company)
        context["round_tours_count"] = self.round_tours_count(company)

        return context


class RideCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "create-ride.html"
    form_class = RideForm
    model = Ride

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.company = self.request.user.company
        form.save()
        return redirect("ride:ride_list")


class RideUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "update-ride.html"
    form_class = RideForm
    model = Ride
    context_object_name = "ride"
    success_url = reverse_lazy("ride:ride_list")

    def get_queryset(self) -> models.query.QuerySet[Any]:
        return Ride.objects.filter(
            company=self.request.user.company,
        )
