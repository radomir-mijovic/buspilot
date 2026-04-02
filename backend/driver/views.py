from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import DriverForm
from .models import Driver


class DriverEditFormView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    template_name = "partials/driver-edit-form.html"

    def get_queryset(self):
        return Driver.objects.filter(company=self.request.user.company)


class DriverListView(LoginRequiredMixin, generic.ListView):
    template_name = "drivers.html"
    context_object_name = "drivers"

    def get_queryset(self):
        return Driver.objects.filter(
            company=self.request.user.company,
        ).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DriverForm()
        return context


class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = DriverForm
    model = Driver
    template_name = "drivers.html"
    success_url = reverse_lazy("driver:drivers")

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        driver = form.save()

        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                "partials/driver-row.html",
                {"driver": driver},
            )

        return redirect("driver:drivers")

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect("driver:drivers")


class DriverUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = DriverForm
    model = Driver
    template_name = "drivers.html"
    success_url = reverse_lazy("driver:drivers")

    def get_queryset(self):
        return Driver.objects.filter(
            company=self.request.user.company,
        )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        driver = form.save()

        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                "partials/driver-row.html",
                {"driver": driver},
            )

        return redirect("driver:drivers", pk=driver.pk)


class DriverDeleteView(LoginRequiredMixin, generic.DeleteView):
    success_url = reverse_lazy("driver:drivers")
    template_name = "drivers.html"

    def get_queryset(self) -> models.query.QuerySet[Any]:
        return Driver.objects.filter(
            company=self.request.user.company,
        )

    def post(self, request, *args, **kwargs):
        driver = self.get_object()
        driver.delete()
        if request.headers.get("HX-Request"):
            return HttpResponse(status=200)
        return redirect("driver:drivers")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
