from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
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
        messages.success(self.request, "Vozilo je uspješno dodano.")
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                label = form.fields[field].label if field in form.fields else field
                messages.error(
                    self.request,
                    f"{label}: {error}",
                    extra_tags="vehicle-error",
                )

        return redirect("vehicle:vehicles")
