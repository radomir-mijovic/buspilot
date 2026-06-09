from django.db import models

from common.models import CreatedUpdatedAtTimestampMixin


class Defect(CreatedUpdatedAtTimestampMixin, models.Model):
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
        related_name="defects",
    )
    description = models.TextField()
    is_fixed = models.BooleanField(default=False, blank=True)
    reported_by = models.ForeignKey(
        "driver.Driver",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reported_defects",
    )
    vehicle = models.ForeignKey(
        "vehicle.Vehicle",
        on_delete=models.CASCADE,
        related_name="defects",
    )

    def __str__(self) -> str:
        return (
            f"Defect #{self.pk} - {self.vehicle}"
            if self.vehicle
            else f"Defect #{self.pk}"
        )

    class Meta:
        ordering = ["-created_at"]
