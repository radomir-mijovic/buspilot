from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import GuideForm
from .models import Guide


class GuideEditFormView(LoginRequiredMixin, generic.DetailView):
    model = Guide
    template_name = "partials/guide-edit-form.html"

    def get_queryset(self):
        return Guide.objects.filter(company=self.request.user.company)


class GuideListView(LoginRequiredMixin, generic.ListView):
    template_name = "guides.html"
    context_object_name = "guides"

    def get_queryset(self):
        return Guide.objects.filter(
            company=self.request.user.company,
        ).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GuideForm()
        return context


class GuideCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = GuideForm
    model = Guide
    template_name = "guides.html"
    success_url = reverse_lazy("guide:guides")

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        guide = form.save()

        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                "partials/guide-row.html",
                {"guide": guide},
            )

        return redirect("guide:guides")

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect("guide:guides")


class GuideUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = GuideForm
    model = Guide
    template_name = "guides.html"
    success_url = reverse_lazy("guide:guides")

    def get_queryset(self):
        return Guide.objects.filter(
            company=self.request.user.company,
        )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        guide = form.save()

        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                "partials/guide-row.html",
                {"guide": guide},
            )

        return redirect("guide:guides")

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return redirect("guide:guides")


class GuideDeleteView(LoginRequiredMixin, generic.DeleteView):
    success_url = reverse_lazy("guide:guides")
    template_name = "guides.html"

    def get_queryset(self) -> models.query.QuerySet[Any]:
        return Guide.objects.filter(
            company=self.request.user.company,
        )

    def post(self, request, *args, **kwargs):
        guide = self.get_object()
        guide.delete()

        if request.headers.get("HX-Request"):
            return HttpResponse(status=200)

        return redirect("guide:guides")
