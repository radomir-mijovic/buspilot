from django.db import models
from django_countries.fields import CountryField

from common.models import UIStyleAbstarct
from ride.models import Ride


class RidePropertyManager(models.Model):
    class Meta:
        abstract = True

    @property
    def rides_to_come_count(self) -> int:
        return (
            Ride.rides.from_today_and_on()
            .filter(
                agency=self,
                company=self.company,
            )
            .count()
        )

    @property
    def pass_rides_count(self) -> int:
        return (
            Ride.rides.past_rides()
            .filter(
                agency=self,
                company=self.company,
            )
            .count()
        )


class Agency(
    UIStyleAbstarct,
    RidePropertyManager,
    models.Model,
):
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
        related_name="agencies",
    )
    ceo = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    country = CountryField(blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    mobile_phone_number = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Agency"
        ordering = ("name",)

    def save(self, *args, **kwargs) -> None:
        self.check_card_color_header()
        super().save(*args, **kwargs)
