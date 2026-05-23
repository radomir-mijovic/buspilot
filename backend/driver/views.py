from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import generic

from auth.decorators import admin_permission_required
from auth.models import UserTypeChoices
from company.mixins import SetCompanyInKwargsMixin
from defect.forms import DefectForm
from driver.documents.forms import DriverDocumentUploadForm
from ride.forms import RideDateSearchForm
from ride.models import Ride

from .forms import DriverForm
from .mixins import DriverQueryFilterMixin
from .models import Driver


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class DriverListView(
    LoginRequiredMixin,
    DriverQueryFilterMixin,
    generic.ListView,
):
    template_name = "drivers.html"
    context_object_name = "drivers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DriverForm()
        return context


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class DriverDetailView(
    LoginRequiredMixin,
    DriverQueryFilterMixin,
    generic.DetailView,
):
    template_name = "driver-details.html"
    context_object_name = "driver"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        instance = self.get_object()
        context = super().get_context_data(**kwargs)
        context["form"] = DriverForm(instance=instance)
        context["document_form"] = DriverDocumentUploadForm()
        return context


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class DriverCreateView(
    LoginRequiredMixin,
    DriverQueryFilterMixin,
    generic.CreateView,
):
    form_class = DriverForm
    model = Driver
    template_name = "drivers.html"
    success_url = reverse_lazy("driver:drivers")

    def form_valid(self, form):
        form.instance.company = self.company
        form.instance.user_type = UserTypeChoices.DRIVER
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


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class DriverUpdateView(
    LoginRequiredMixin,
    DriverQueryFilterMixin,
    generic.UpdateView,
):
    form_class = DriverForm
    model = Driver
    template_name = "driver-details.html"
    context_object_name = "driver"

    def get_success_url(self) -> str:
        return reverse(
            "driver:driver_details",
            kwargs={"pk": self.get_object().pk},
        )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(
            self.request,
            _("Data successfully updated"),
        )
        return super().form_valid(form)


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class DriverDeleteView(
    LoginRequiredMixin,
    DriverQueryFilterMixin,
    generic.DeleteView,
):
    success_url = reverse_lazy("driver:drivers")
    template_name = "drivers.html"

    def get(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse:
        return self.delete(request, *args, **kwargs)


class DriverRidesView(
    SetCompanyInKwargsMixin,
    LoginRequiredMixin,
    generic.ListView,
):
    context_object_name = "rides"
    model = Ride
    template_name = "driver-rides.html"

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["defect_form"] = DefectForm(company=self.company)
        context["form"] = RideDateSearchForm()
        return context

    def get_queryset(self):
        today = timezone.now().date()
        qs = self.get_base_queryset()

        if start_date := self.request.GET.get("start_date"):
            return qs.filter(start_date=start_date)

        return qs.filter(start_date__gte=today)

    def get_base_queryset(self):
        return (
            Ride.objects.filter(drivers=self.request.user)
            .order_by("start_time", "start_date")
            .select_related("agency")
        )
