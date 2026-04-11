import random
from django.db import models

HEADERS_COLORS: list[str] = [
    "danger",
    "info",
    "warning",
    "secondary",
    "primary",
    "success",
    "purple",
    "pink",
    "teal",
    "orange",
]

class CreatedUpdatedAtTimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeSlot(models.Model):
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        abstract = True


class DateSlot(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True


class LocationSlot(models.Model):
    start_location = models.CharField(max_length=255, blank=True)
    end_location = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class PersonAbstract(models.Model):
    company = models.ForeignKey(
        "company.Company",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_items",
    )
    email = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True)
    passport_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.last_name + " " + self.first_name

    class Meta:
        abstract = True


class UIStyleAbstarct(models.Model):
    card_header_color = models.CharField(max_length=20, blank=True)

    class Meta:
        abstract = True

    def check_card_color_header(self) -> None:
        if not self.card_header_color or not self.card_header_color_is_valid_option():
            self.assing_card_header_color()

    def card_header_color_is_valid_option(self) -> bool:
        return self.card_header_color in HEADERS_COLORS

    def assing_card_header_color(self) -> None:
        self.card_header_color = self.get_random_color()

    def get_random_color(self) -> str:
        return random.choice(HEADERS_COLORS)
