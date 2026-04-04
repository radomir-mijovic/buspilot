from django.forms import ModelForm

from ..models import VehicleDocument


class VehicleDocumentUploadForm(ModelForm):
    class Meta:
        model = VehicleDocument
        fields = [
            "title",
            "document_type",
            "expiring_at",
            "file",
        ]
