from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from ..models import Vehicle, VehicleDocument
from .forms import VehicleDocumentUploadForm


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


class VehicleDocumentUploadView(
    VehicleHtmxFormsViewHandlers,
    LoginRequiredMixin,
):
    form_class = VehicleDocumentUploadForm
    model = VehicleDocument
    template_name = "../templates/vehicle-details.html"

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
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


class VehicleDocumentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "../templates/vehicle-details.html"

    def get_queryset(self):
        return VehicleDocument.objects.filter(
            vehicle__company=self.request.user.company
        )

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        vehicle_pk = instance.vehicle.pk
        instance.delete()

        if request.headers.get("HX-Request"):
            return HttpResponse(status=200)

        return redirect("vehicle:vehicles_details", pk=vehicle_pk)
