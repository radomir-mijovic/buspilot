from django.db import models


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
    engine_number = models.CharField(max_length=100, blank=True)
    horse_power = models.CharField(max_length=100, blank=True)
    licence_number = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100)
    number_of_seats = models.CharField(max_length=20, blank=True)
    year_of_production = models.CharField(max_length=100, blank=True)
    vehicle_type = models.CharField(max_length=100, blank=True, choices=VEHICLE_TYPE_CHOICES)
    weight = models.CharField(max_length=100, blank=True, help_text="weight in KG")

    def __str__(self):
        return str(self.brand) + str(self.model)


# class VehicleDocument(models.Model):
#    document_type = models.CharField(max_length=100)
