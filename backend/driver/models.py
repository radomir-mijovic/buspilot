from django.db import models


class Driver(models.Model):
    company = models.ForeignKey(
        "company.Company",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="drivers",
    )
    email = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True)
    passport_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.last_name + " " + self.first_name
