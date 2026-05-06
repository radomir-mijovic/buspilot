from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from auth.decorators import admin_permission_required
from auth.models import UserTypeChoices

from .forms import GuideForm
from .mixins import GuideQueryFilterMixin
from .models import Guide


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class GuideEditFormView(
    LoginRequiredMixin,
    GuideQueryFilterMixin,
    generic.DetailView,
):
    model = Guide
    template_name = "partials/guide-edit-form.html"


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class GuideListView(
    LoginRequiredMixin,
    GuideQueryFilterMixin,
    generic.ListView,
):
    template_name = "guides.html"
    context_object_name = "guides"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GuideForm()
        return context


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class GuideCreateView(
    LoginRequiredMixin,
    GuideQueryFilterMixin,
    generic.CreateView,
):
    form_class = GuideForm
    model = Guide
    template_name = "guides.html"
    success_url = reverse_lazy("guide:guides")

    def form_valid(self, form):
        form.instance.company = self.company
        form.instance.user_type = UserTypeChoices.GUIDE
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


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class GuideUpdateView(
    LoginRequiredMixin,
    GuideQueryFilterMixin,
    generic.UpdateView,
):
    form_class = GuideForm
    model = Guide
    template_name = "guides.html"
    success_url = reverse_lazy("guide:guides")

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


@method_decorator(
    admin_permission_required,
    name="dispatch",
)
class GuideDeleteView(
    LoginRequiredMixin,
    GuideQueryFilterMixin,
    generic.DeleteView,
):
    success_url = reverse_lazy("guide:guides")
    template_name = "guides.html"

    def post(self, request, *args, **kwargs):
        guide = self.get_object()
        guide.delete()

        if request.headers.get("HX-Request"):
            return HttpResponse(status=200)

        return redirect("guide:guides")
