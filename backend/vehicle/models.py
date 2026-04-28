from django.core.validators import FileExtensionValidator
from django.db import models

from common.models import DocumentAbstract, VALID_FILE_EXTENSIONS
from ride.models import Ride

from . import constants



class VehicleTypeChoices(models.IntegerChoices):
    CAR = constants.CAR, "Car"
    VAN = constants.VAN, "Van"
    MINI_BUS = constants.MINI_BUS, "Mini Bus"
    MIDI_BUS = constants.MIDI_BUS, "Midi Bus"
    BUS = constants.BUS, "Bus"


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
        blank=True,
        related_name="vehicles",
    )
    chassis_number = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    driver = models.ManyToManyField(
        "driver.Driver",
        blank=True,
        related_name="vehicles",
    )
    engine_number = models.CharField(max_length=100, blank=True)
    horse_power = models.CharField(max_length=100, blank=True)
    licence_number = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100)
    number_of_seats = models.CharField(max_length=20, blank=True)
    year_of_production = models.CharField(max_length=100, blank=True)
    vehicle_type = models.PositiveIntegerField(
        blank=True,
        choices=VehicleTypeChoices,
    )
    weight = models.CharField(max_length=100, blank=True, help_text="weight in KG")

    def __str__(self):
        return str(self.brand) + " " + str(self.model) + " " + self.number_of_seats

    @property
    def all_documents(self):
        """Using it for templates"""
        return self.documents.all()

    @property
    def today_rides(self):
        return Ride.rides.today().filter(
            vehicles=self,
            company=self.company,
        )

    @property
    def tomorrow_rides(self):
        return Ride.rides.tomorrow().filter(
            company=self.company,
            vehicles=self,
        )

    @property
    def after_tomorrow_rides(self):
        return Ride.rides.after_tomorrow().filter(
            company=self.company,
            vehicles=self,
        )

    @property
    def rides_count(self) -> int:
        return (
            Ride.rides.from_today_and_on()
            .filter(
                company=self.company,
                vehicles=self,
            )
            .count()
        )


class VehicleDocument(DocumentAbstract):
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
