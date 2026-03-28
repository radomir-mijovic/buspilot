from django.contrib.auth.forms import PasswordChangeForm


def change_password_form(request):
    if request.user.is_authenticated:
        return {"change_password_form": PasswordChangeForm}
    return {}
