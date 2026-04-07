from django.core.validators import FileExtensionValidator
from django.db import models

from common.models import CreatedUpdatedAtTimestampMixin

VALID_FILE_EXTENSIONS = ["pdf", "jpg", "jpeg", "png", "docx", "txt", "xlsx"]


class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ("Bus", "Bus"),
        ("Van", "Van"),
        ("Car", "Car"),
    ]

    brand = models.CharField(max_length=100)
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    chassis_number = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    driver = models.ManyToManyField("driver.Driver", related_name="vehicles", blank=True,)
    engine_number = models.CharField(max_length=100, blank=True)
    horse_power = models.CharField(max_length=100, blank=True)
    licence_number = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100)
    number_of_seats = models.CharField(max_length=20, blank=True)
    year_of_production = models.CharField(max_length=100, blank=True)
    vehicle_type = models.CharField(
        max_length=100, blank=True, choices=VEHICLE_TYPE_CHOICES
    )
    weight = models.CharField(max_length=100, blank=True, help_text="weight in KG")

    def __str__(self):
        return str(self.brand) + " " + str(self.model) + " " + self.number_of_seats

    @property
    def all_documents(self):
        """Using it for templates"""
        return self.documents.all()


class VehicleDocument(CreatedUpdatedAtTimestampMixin, models.Model):
    title = models.CharField(max_length=255, blank=True)
    document_type = models.CharField(max_length=255, blank=True)
    expiring_at = models.DateField(blank=True, null=True)
    file = models.FileField(
        upload_to="vehicle/documents/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=VALID_FILE_EXTENSIONS,
            ),
        ],
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        blank=True,
        related_name="documents",
    )

    def __str__(self):
        return self.title

    def get_file_size(self) -> float:
        if self.file:
            return self.file.size
        return 0

    def file_size_kb(self) -> float:
        return self.get_file_size() / 1024

    def file_size_mb(self) -> float:
        return self.file_size_kb() / 1024
