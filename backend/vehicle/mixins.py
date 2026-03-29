from django.contrib import messages
from django.http import HttpResponse


class VehicleViewMixin:
    def _get_hx_field_errors(self, form):
        errors = []
        for field, errs in form.errors.items():
            label = form.fields[field].label if field in form.fields else field
            for error in errs:
                errors.append(f"{label}: {error}")
        return errors

    def _return_partials_http_response(self, errors):
        return HttpResponse(b", ".join(errors), status=422)

    def _handle_form_partials_errors(self, form):
        errors = self._get_hx_field_errors(form)
        return self._return_partials_http_response(errors)

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
