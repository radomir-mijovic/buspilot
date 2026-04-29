import random
from datetime import timedelta

from django.db import models
from django.utils import timezone

from company.models import Company

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

VALID_FILE_EXTENSIONS = [
    "pdf",
    "jpg",
    "jpeg",
    "png",
    "docx",
    "txt",
    "xlsx",
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

    def check_card_color_header(self) -> None:
        if not self.card_header_color or not self.card_header_color_is_valid_option():
            self.assing_card_header_color()

    def card_header_color_is_valid_option(self) -> bool:
        return self.card_header_color in HEADERS_COLORS

    def assing_card_header_color(self) -> None:
        self.card_header_color = self.get_random_color()

    def get_random_color(self) -> str:
        return random.choice(HEADERS_COLORS)

    class Meta:
        abstract = True


class DocumentManager(models.Manager):
    def close_to_expire(self):
        return self.filter(
            expiring_at__gte=self.today_date(),
            expiring_at__lte=self.one_month_ahead(),
        ).order_by("expiring_at")

    def one_month_ahead(self):
        one_month_ahead_date = self.today_date() + timedelta(days=30)
        return one_month_ahead_date

    def today_date(self):
        return timezone.now().date()


class DocumentAbstract(
    CreatedUpdatedAtTimestampMixin,
    DocumentManager,
):
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="%(class)s_documents",
    )
    title = models.CharField(max_length=255, blank=True)
    document_type = models.CharField(max_length=255, blank=True)
    expiring_at = models.DateField(blank=True, null=True)

    expiring = DocumentManager()

    def __str__(self):
        return self.title

    def get_file_size(self) -> float:
        return self.file.size if self.file else 0

    def file_size_kb(self) -> float:
        return self.get_file_size() / 1024

    def file_size_mb(self) -> float:
        return self.file_size_kb() / 1024

    @property
    def has_expired(self) -> bool:
        return self.expiring_at < timezone.now().date()

    @property
    def days_to_expire(self) -> int | None:
        if not self.expiring_at:
            return None
        return (self.expiring_at - timezone.now().date()).days

    class Meta:
        abstract = True
