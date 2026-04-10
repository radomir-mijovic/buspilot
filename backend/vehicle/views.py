from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from vehicle.documents.forms import VehicleDocumentUploadForm

from .forms import VehicleCreateForm
from .models import Vehicle


class VehicleView(LoginRequiredMixin, generic.ListView):
    template_name = "vehicle.html"
    context_object_name = "vehicles"

    def get_queryset(self):
        return Vehicle.objects.filter(
            company=self.request.user.company,
        ).select_related("company")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = VehicleCreateForm()
        return context


class VehicleDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "vehicle-details.html"
    context_object_name = "vehicle"

    def get_queryset(self):
        return (
            Vehicle.objects.filter(
                company=self.request.user.company,
            )
            .select_related("company")
            .prefetch_related("documents")
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = VehicleCreateForm(instance=self.object)
        context["document_form"] = VehicleDocumentUploadForm()
        return context


class VehicleCreateView(
    LoginRequiredMixin,
    generic.CreateView,
):
    model = Vehicle
    form_class = VehicleCreateForm
    success_url = reverse_lazy("vehicle:vehicles")

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        vehicle = form.save()

        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                "partials/vehicle_row.html",
                {"vehicle": vehicle},
            )

        return redirect("vehicle:vehicles")

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect("vehicle:vehicles")


class VehicleUpdateView(
    LoginRequiredMixin,
    generic.UpdateView,
):
    model = Vehicle
    form_class = VehicleCreateForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        vehicle = form.save()

        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                "partials/vehicle_details_row.html",
                {"vehicle": vehicle},
            )

        return redirect("vehicle:vehicles_details", pk=vehicle.pk)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        vehicle = self.get_object()
        return redirect(
            "vehicle:vehicles_details",
            pk=vehicle.pk,
        )


class VehicleDeleteView(
    LoginRequiredMixin,
    generic.DeleteView,
):
    model = Vehicle
    success_url = reverse_lazy("vehicle:vehicles")

    def get_queryset(self):
        return Vehicle.objects.filter(company=self.request.user.company)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        if request.headers.get("HX-Request"):
            return HttpResponse(status=200)

        return redirect("vehicle:vehicles")
