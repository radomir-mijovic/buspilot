from django.db import models
from django_countries.fields import CountryField


class RequestDemo(models.Model):
    company = models.CharField()
    country = CountryField()
    email = models.EmailField()
    contact_number = models.CharField()

    def __str__(self) -> str:
        return self.company

    class Meta:
        verbose_name_plural = "Request Demo"
