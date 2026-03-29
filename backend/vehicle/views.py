from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import VehicleCreateForm
from .mixins import VehicleViewMixin
from .models import Vehicle


class VehicleView(LoginRequiredMixin, generic.ListView):
    template_name = "vehicle.html"
    context_object_name = "vehicles"

    def get_queryset(self):
        return Vehicle.objects.filter(
            company=self.request.user.company,
        ).select_related("company")


class VehicleDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "vehicle-details.html"
    context_object_name = "vehicle"

    def get_queryset(self):
        return Vehicle.objects.filter(
            company=self.request.user.company,
        ).select_related("company")


class VehicleCreateView(LoginRequiredMixin, VehicleViewMixin, generic.CreateView):
    model = Vehicle
    form_class = VehicleCreateForm
    success_url = reverse_lazy("vehicle:vehicles")

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        vehicle = form.save()

        if self.request.headers.get("HX-Request"):
            return self._message_and_render_partials(vehicle)

        return self._message_and_render_template()

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return self._handle_form_partials_errors(form)

        self._handle_form_errors(form)
        return redirect("vehicle:vehicles")

    def _message_and_render_partials(self, vehicle: Vehicle) -> HttpResponse:
        self._self_message_success("Vozilo je uspješno dodano.")
        return render(
            self.request,
            "partials/vehicle_row.html",
            {"vehicle": vehicle, "include_modal": True},
        )

    def _message_and_render_template(
        self,
    ) -> HttpResponsePermanentRedirect | HttpResponseRedirect:
        self._self_message_success("Vozilo je uspješno dodano.")
        return redirect("vehicle:vehicles")


class VehicleUpdateView(LoginRequiredMixin, VehicleViewMixin, generic.UpdateView):
    model = Vehicle
    form_class = VehicleCreateForm

    def form_valid(self, form):
        vehicle = form.save()

        if self.request.headers.get("HX-Request"):
            template = self._get_partial_template()
            return render(self.request, template, {"vehicle": vehicle})

        return redirect("vehicle:vehicles_details", pk=vehicle.pk)

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return self._handle_form_partials_errors(form)

        self._handle_form_errors(form)
        vehicle = self.get_object()
        return redirect("vehicle:vehicles_details", pk=vehicle.id)

    def _get_partial_template(self):
        template = "partials/vehicle_details_row.html"
        return template


class VehicleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy("vehicle:vehicles")

    def get_queryset(self):
        return Vehicle.objects.filter(company=self.request.user.company)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        if request.headers.get("HX-Request"):
            return HttpResponse(status=200)
        return redirect(self.success_url)
