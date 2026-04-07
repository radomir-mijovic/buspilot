from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import RideForm
from .models import Ride


class RideCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "create-ride.html"
    form_class = RideForm
    model = Ride

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.company = self.request.user.company
        form.save()
        return redirect("dashboard:dashboard")


class RideUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "update-ride.html"
    form_class = RideForm
    model = Ride
    context_object_name = "ride"
    success_url = reverse_lazy("dashboard:dashboard")

    def get_queryset(self) -> models.query.QuerySet[Any]:
        return Ride.objects.filter(
            company=self.request.user.company,
        )
