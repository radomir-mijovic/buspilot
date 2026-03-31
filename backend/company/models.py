from django.db import models


# TODO: add logo when you setup claud service
class Company(models.Model):
    email = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=255, blank=True)
    tax_id = models.CharField(
        max_length=100,
        blank=True,
        help_text="Tax Identification Number (PIB)",
    )
    vat = models.CharField(
        max_length=100,
        blank=True,
        help_text="Value Added Tax (PDV)",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Company"


class CompanyAddress(models.Model):
    city = models.CharField(max_length=255, blank=True)
    company = models.ForeignKey(
        Company,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="addresses",
    )
    country = models.CharField(max_length=255, blank=True)
    country_code = models.CharField(max_length=3, blank=True)
    post_code = models.CharField(max_length=100, blank=True)
    state_province = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255, blank=True)
    street_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.company.name + self.city
