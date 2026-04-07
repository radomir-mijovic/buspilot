from datetime import timedelta

from django.db import models
from django.utils import timezone

from company.models import Company

from . import constants


class RideDateManager(models.Manager):
    def today(self):
        return self.filter(start_date=self.today_date())

    def tomorrow(self):
        return self.filter(start_date=self.tomorrow_date())

    def after_tomorrow(self):
        return self.filter(start_date__gt=self.tomorrow_date())

    def from_today_and_on(self):
        return self.filter(start_date__gte=self.today_date())

    def past_rides(self):
        return self.filter(start_date__lt=self.today_date())

    def today_date(self):
        return timezone.now().date()

    def tomorrow_date(self):
        today = timezone.now().date()
        tomorrow = today + timedelta(days=1)
        return tomorrow


class RideLineManager(RideDateManager):
    def today(self, company: Company):
        return (
            super()
            .today()
            .filter(
                ride_type=constants.LINE,
                company=company,
            )
        )

    def tomorrow(self, company: Company):
        return (
            super()
            .tomorrow()
            .filter(
                ride_type=constants.LINE,
                company=company,
            )
        )

    def after_tomorrow(self, company: Company):
        return (
            super()
            .after_tomorrow()
            .filter(
                ride_type=constants.LINE,
                company=company,
            )
        )


class RideTransferManager(RideDateManager):
    def today(self, company: Company):
        return (
            super()
            .today()
            .filter(
                ride_type=constants.TRANSFER,
                company=company,
            )
        )

    def tomorrow(self, company: Company):
        return (
            super()
            .tomorrow()
            .filter(
                ride_type=constants.TRANSFER,
                company=company,
            )
        )

    def after_tomorrow(self, company: Company):
        return (
            super()
            .after_tomorrow()
            .filter(
                ride_type=constants.TRANSFER,
                company=company,
            )
        )


class RideExcursionManager(RideDateManager):
    def today(self, company: Company):
        return (
            super()
            .today()
            .filter(
                ride_type=constants.EXCURSION,
                company=company,
            )
        )

    def tomorrow(self, company: Company):
        return (
            super()
            .tomorrow()
            .filter(
                ride_type=constants.EXCURSION,
                company=company,
            )
        )

    def after_tomorrow(self, company: Company):
        return (
            super()
            .after_tomorrow()
            .filter(
                ride_type=constants.EXCURSION,
                company=company,
            )
        )


class RideRoundTourManager(RideDateManager):
    def today(self, company: Company):
        return (
            super()
            .today()
            .filter(
                ride_type=constants.ROUND_TOUR,
                company=company,
            )
        )

    def tomorrow(self, company: Company):
        return (
            super()
            .tomorrow()
            .filter(
                ride_type=constants.ROUND_TOUR,
                company=company,
            )
        )

    def after_tomorrow(self, company: Company):
        return (
            super()
            .after_tomorrow()
            .filter(
                ride_type=constants.ROUND_TOUR,
                company=company,
            )
        )
