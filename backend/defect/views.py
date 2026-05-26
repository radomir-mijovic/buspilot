from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View, generic

from company.mixins import CompanyRequestMixin
from vehicle.models import Vehicle

from .forms import DefectForm
from .mixins import DefectQueryFilterMixin
from .models import Defect


class DefectListView(
    DefectQueryFilterMixin,
    LoginRequiredMixin,
    generic.ListView,
):
    template_name = "defects.html"
    context_object_name = "defects"
    model = Defect

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["vehicles"] = Vehicle.objects.filter(
            defects__isnull=False,
            company=self.company,
        ).distinct()
        context["active_defects"] = self.get_defects(self.request, is_fixed=False)
        context["resolved_defects"] = self.get_defects(self.request, is_fixed=True)
        return context

    def get_queryset(self) -> models.QuerySet[Defect]:
        return Defect.objects.filter(
            company=self.company,
        ).select_related("vehicle", "reported_by")

    def get_defects(
        self,
        request,
        *,
        is_fixed: bool | None = None,
    ) -> models.QuerySet[Defect]:
        defects = Defect.objects.filter(is_fixed=is_fixed, company=self.company)

        if vehicle_pk := request.GET.get("vehicle"):
            return defects.filter(vehicle__pk=vehicle_pk)

        return defects


class DefectMarkAsResolved(
    DefectQueryFilterMixin,
    LoginRequiredMixin,
    View,
):
    def post(self, request, *args, **kwargs):
        is_fixed = request.POST.get("is_fixed")
        self.update_is_fixed_field(is_fixed)
        messages.success(request, _("Defect updated successfully."))
        return redirect("defect:defects")

    @property
    def defect(self):
        defect = get_object_or_404(
            Defect,
            pk=self.kwargs.get("pk"),
            company=self.company,
        )
        return defect

    def update_is_fixed_field(self, is_fixed: bool) -> None:
        defect = self.defect
        defect.is_fixed = is_fixed
        defect.save(update_fields=["is_fixed"])


class DefectCreateView(
    CompanyRequestMixin,
    LoginRequiredMixin,
    generic.CreateView,
):
    form_class = DefectForm

    def get_success_url(self) -> str:
        driver = self.request.user
        return reverse("driver:driver_rides", args=[driver.pk])

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        driver = self.request.user
        form.instance.company = self.company
        form.instance.reported_by = driver
        form.save()
        messages.success(self.request, _("Defect successfully reported."))
        return redirect("driver:driver_rides")


class DefectDeleteView(
    DefectQueryFilterMixin,
    LoginRequiredMixin,
    generic.DeleteView,
):
    model = Defect
    success_url = reverse_lazy("defect:defects")

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        messages.success(request, _("Defect successfully deleted."))
        return redirect("defect:defects")
