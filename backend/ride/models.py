from django.db import models

from common.models import DateSlot, LocationSlot, TimeSlot

from . import constants, managers


class RideTypeChoices(models.IntegerChoices):
    LINE = constants.LINE, "Line"
    TRANSFER = constants.TRANSFER, "Transfer"
    EXCURSION = constants.EXCURSION, "Excursion"
    ROUND_TOUR = constants.ROUND_TOUR, "Round Tour"


class RideQueryManager(models.Model):
    rides = managers.RideDateManager()
    lines = managers.RideLineManager()
    transfers = managers.RideTransferManager()
    excursions = managers.RideExcursionManager()
    round_tours = managers.RideRoundTourManager()

    class Meta:
        abstract = True


class RideManyToManyManager(models.Model):
    drivers = models.ManyToManyField(
        "driver.Driver",
        blank=True,
        related_name="rides",
    )
    guides = models.ManyToManyField(
        "guide.Guide",
        blank=True,
        related_name="rides",
    )
    vehicles = models.ManyToManyField(
        "vehicle.Vehicle",
        blank=True,
        related_name="rides",
    )

    class Meta:
        abstract = True


class Ride(
    DateSlot,
    LocationSlot,
    TimeSlot,
    RideManyToManyManager,
    RideQueryManager,
):
    agency = models.ForeignKey(
        "agency.Agency",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    is_all_day = models.BooleanField(default=False)
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
        related_name="rides",
    )
    description = models.TextField(blank=True)
    ride_type = models.PositiveSmallIntegerField(
        choices=RideTypeChoices,
        blank=True,
    )
    title = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Ride"
