from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    chassis_number = models.CharField(max_length=100, blank=True)
    engine_number = models.CharField(max_length=100, blank=True)
    horse_power = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100)
    year_of_production = models.CharField(max_length=100, blank=True)
    vehicle_type = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=100, blank=True, help_text="weight in KG")

    def __str__(self):
        return str(self.brand) + str(self.model)


#class VehicleDocument(models.Model):
#    document_type = models.CharField(max_length=100)
