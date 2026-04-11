from datetime import timedelta

from django.db import models
from django.utils import timezone


from . import constants


class RideDateManager(models.Manager):
    def today(self):
        return (
            self.filter(
                start_date=self.today_date(),
            )
            .prefetch_related("vehicles", "drivers")
            .order_by("start_time")
        )

    def tomorrow(self):
        return (
            self.filter(
                start_date=self.tomorrow_date(),
            )
            .prefetch_related("vehicles", "drivers")
            .order_by("start_time")
        )

    def after_tomorrow(self):
        return (
            self.filter(
                start_date__gt=self.tomorrow_date(),
            )
            .prefetch_related("vehicles", "drivers")
            .order_by("start_date", "start_time")
        )

    def from_today_and_on(self):
        return (
            self.filter(
                start_date__gte=self.today_date(),
            )
            .prefetch_related("vehicles", "drivers")
            .order_by("start_date", "start_time")
        )

    def past_rides(self):
        return (
            self.filter(
                start_date__lt=self.today_date(),
            )
            .prefetch_related("vehicles", "drivers")
            .order_by("-start_date", "-start_time")
        )

    def today_date(self):
        return timezone.now().date()

    def tomorrow_date(self):
        today = timezone.now().date()
        tomorrow = today + timedelta(days=1)
        return tomorrow


class RideLineManager(RideDateManager):
    def today(self):
        return (
            super()
            .today()
            .filter(
                ride_type=constants.LINE,
            )
        )

    def tomorrow(self):
        return (
            super()
            .tomorrow()
            .filter(
                ride_type=constants.LINE,
            )
        )

    def after_tomorrow(self):
        return (
            super()
            .after_tomorrow()
            .filter(
                ride_type=constants.LINE,
            )
        )

    def from_today_and_on(self):
        return (
            super()
            .from_today_and_on()
            .filter(
                ride_type=constants.LINE,
            )
        )


class RideTransferManager(RideDateManager):
    def today(self):
        return (
            super()
            .today()
            .filter(
                ride_type=constants.TRANSFER,
            )
        )

    def tomorrow(self):
        return (
            super()
            .tomorrow()
            .filter(
                ride_type=constants.TRANSFER,
            )
        )

    def after_tomorrow(self):
        return (
            super()
            .after_tomorrow()
            .filter(
                ride_type=constants.TRANSFER,
            )
        )

    def from_today_and_on(self):
        return (
            super()
            .from_today_and_on()
            .filter(
                ride_type=constants.TRANSFER,
            )
        )


class RideExcursionManager(RideDateManager):
    def today(self):
        return (
            super()
            .today()
            .filter(
                ride_type=constants.EXCURSION,
            )
        )

    def tomorrow(self):
        return (
            super()
            .tomorrow()
            .filter(
                ride_type=constants.EXCURSION,
            )
        )

    def after_tomorrow(self):
        return (
            super()
            .after_tomorrow()
            .filter(
                ride_type=constants.EXCURSION,
            )
        )

    def from_today_and_on(self):
        return (
            super()
            .from_today_and_on()
            .filter(
                ride_type=constants.EXCURSION,
            )
        )


class RideRoundTourManager(RideDateManager):
    def today(self):
        return (
            super()
            .today()
            .filter(
                ride_type=constants.ROUND_TOUR,
            )
        )

    def tomorrow(self):
        return (
            super()
            .tomorrow()
            .filter(
                ride_type=constants.ROUND_TOUR,
            )
        )

    def after_tomorrow(self):
        return (
            super()
            .after_tomorrow()
            .filter(
                ride_type=constants.ROUND_TOUR,
            )
        )

    def from_today_and_on(self):
        return (
            super()
            .from_today_and_on()
            .filter(
                ride_type=constants.ROUND_TOUR,
            )
        )

