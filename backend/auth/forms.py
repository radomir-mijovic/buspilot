from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Unesite username",
                "id": "username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control pe-5 password-input",
                "placeholder": "Unesite password",
                "id": "password-input",
            }
        )
    )


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + (
            "phone_number",
            "passport_number",
        )
