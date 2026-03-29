from django.contrib import messages
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


class VehicleCreateView(LoginRequiredMixin, generic.CreateView):
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
            errors = []
            for field, errs in form.errors.items():
                label = form.fields[field].label if field in form.fields else field
                for error in errs:
                    errors.append(f"{label}: {error}")
            return HttpResponse(b", ".join(errors), status=422)

        self._handle_form_errors(form)
        return redirect("vehicle:vehicles")

    def _message_and_render_partials(self, vehicle: Vehicle) -> HttpResponse:
        self._self_message_success()
        return render(self.request, "partials/vehicle_row.html", {"vehicle": vehicle})

    def _message_and_render_template(
        self,
    ) -> HttpResponsePermanentRedirect | HttpResponseRedirect:
        self._self_message_success()
        return redirect("vehicle:vehicles")

    def _handle_form_errors(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                label = self._generate_labels(form, field)
                self._self_message_error(label, error)

    def _generate_labels(self, form, field):
        label = form.fields[field].label if field in form.fields else field
        return label

    def _self_message_error(self, label: str, error: str) -> None:
        messages.error(self.request, f"{label}: {error}", extra_tags="vehicle-error")

    def _self_message_success(self) -> None:
        messages.success(self.request, "Vozilo je uspješno dodano.")


class VehicleUpdateView(LoginRequiredMixin, generic.UpdateView):
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
            errors = self._get_hx_field_errors(form)
            return HttpResponse(b", ".join(errors), status=422)

        for field, errors in form.errors.items():
            for error in errors:
                label = form.fields[field].label if field in form.fields else field
                messages.error(
                    self.request, f"{label}: {error}", extra_tags="vehicle-error"
                )

        vehicle = self.get_object()
        return redirect("vehicle:vehicles_details", pk=vehicle.id)

    def _get_partial_template(self):
        template = (
            "partials/vehicle_details_row.html"
            if self.request.POST.get("source") == "details"
            else "partials/vehicle_row.html"
        )
        return template

    @staticmethod
    def _get_hx_field_errors(form):
        errors = []
        for field, errs in form.errors.items():
            label = form.fields[field].label if field in form.fields else field
            for error in errs:
                errors.append(f"{label}: {error}")
        return errors


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
