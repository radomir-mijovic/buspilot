from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string


class VehicleViewMixin:
    def _get_hx_field_errors(self, form):
        errors = []
        for field, errs in form.errors.items():
            label = form.fields[field].label if field in form.fields else field
            for error in errs:
                errors.append(f"{label}: {error}")
        return errors

    def _render_messages_oob(self):
        return render_to_string("partials/toast_messages.html", request=self.request)

    def _handle_form_partials_errors(self, form):
        for error in self._get_hx_field_errors(form):
            messages.error(self.request, error, extra_tags="vehicle-error")
        response = HttpResponse(self._render_messages_oob())
        response["HX-Reswap"] = "none"
        return response

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

    def _self_message_success(self, msg: str) -> None:
        messages.success(self.request, msg)
