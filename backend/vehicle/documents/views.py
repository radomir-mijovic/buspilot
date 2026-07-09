from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.views import generic

from auth.decorators import admin_permission_required
from company.mixins import CompanyRequestMixin

from ..models import Vehicle, VehicleDocument
from .forms import VehicleDocumentUploadForm


@method_decorator(
    admin_permission_required,
    name="dispatch"
)
class VehicleHtmxFormsViewHandlers(generic.CreateView):
    def handle_form_valid_htmx(
        self,
        document: VehicleDocument,
    ) -> HttpResponse:
        return render(
            self.request,
            "partials/document-row.html",
            {"document": document},
        )

    def handle_form_invalid_htmx(self, form: BaseModelForm) -> HttpResponse:
        response = render(
            self.request,
            "partials/document-upload-form.html",
            {"form": form},
            status=422,
        )
        response["HX-Retarget"] = "#addDocumentModalBody"
        response["HX-Reswap"] = "innerHTML"
        return response


@method_decorator(
    admin_permission_required,
    name="dispatch"
)
class VehicleDocumentUploadView(
    VehicleHtmxFormsViewHandlers,
    CompanyRequestMixin,
    LoginRequiredMixin,
):
    form_class = VehicleDocumentUploadForm
    model = VehicleDocument
    template_name = "../templates/vehicle-details.html"

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
        form.instance.company = self.company
        document = form.save()

        if self.request.headers.get("HX-Request"):
            return self.handle_form_valid_htmx(document)

        return self.redirect_to_vehicle_details()

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return self.handle_form_invalid_htmx(form)

        return self.redirect_to_vehicle_details()

    def redirect_to_vehicle_details(self):
        return redirect("vehicle:vehicles_details", pk=self.vehicle_pk)

    @property
    def vehicle_pk(self):
        return self.kwargs.get("vehicle_pk")

    @property
    def vehicle(self):
        return get_object_or_404(Vehicle, pk=self.vehicle_pk)


@method_decorator(
    admin_permission_required,
    name="dispatch"
)
class VehicleDocumentUpdateView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.UpdateView,
):
    form_class = VehicleDocumentUploadForm
    model = VehicleDocument
    template_name = "../templates/partials/update-vehicle-document-modal.html"

    def get_queryset(self) -> models.query.QuerySet[Any]:
        return VehicleDocument.objects.filter(
            vehicle__company=self.company,
        )

    def form_valid(self, form):
        document = form.save()
        messages.success(self.request, _("Document updated successfully"))
        url = reverse("vehicle:vehicles_details", args=[document.vehicle.pk])
        return redirect(f"{url}#vehicle-documents")

    def form_invalid(self, form):
        document = self.get_object()
        for error in form.errors.values():
            messages.error(self.request, error.as_text())

        url = reverse("vehicle:vehicles_details", args=[document.vehicle.pk])
        return redirect(f"{url}#vehicle-documents")


@method_decorator(
    admin_permission_required,
    name="dispatch"
)
class VehicleDocumentDeleteView(
    LoginRequiredMixin,
    CompanyRequestMixin,
    generic.DeleteView,
):
    template_name = "../templates/vehicle-details.html"

    def get_queryset(self):
        return VehicleDocument.objects.filter(vehicle__company=self.company)

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        vehicle_pk = instance.vehicle.pk
        instance.delete()

        if request.headers.get("HX-Request"):
            return HttpResponse(status=200)

        return redirect("vehicle:vehicles_details", pk=vehicle_pk)
