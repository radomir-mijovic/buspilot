from django.forms import ModelForm

from .models import Guide


class GuideForm(ModelForm):
    class Meta:
        model = Guide
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "passport_number",
        ]
