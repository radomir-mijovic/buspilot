from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from .forms import LoginForm


def login_user(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_admin:
                return redirect("dashboard:dashboard")
            return redirect("driver:drivers")
        else:
            messages.error(request, _("Invalid username or password."))

    return render(request, "login.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, _("You have logged out."))
    return redirect("auth:login")


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _("Password successfully changed"))
        else:
            messages.error(request, _("Please check password"))
            if form.errors:
                for error in form.errors.values():
                    messages.error(request, error.as_text())

    return redirect("dashboard:dashboard")
