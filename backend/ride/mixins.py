from company.models import Company

from .models import Ride


class RidesCountMixin:
    def count_all(self, company: Company):
        return (
            Ride.rides.from_today_and_on()
            .filter(
                company=company,
            )
            .count()
        )

    def transfers_count(self, company: Company) -> int:
        return (
            Ride.transfers.from_today_and_on()
            .filter(
                company=company,
            )
            .count()
        )

    def excursions_count(self, company: Company) -> int:
        return (
            Ride.excursions.from_today_and_on()
            .filter(
                company=company,
            )
            .count()
        )

    def lines_count(self, company: Company) -> int:
        return (
            Ride.lines.from_today_and_on()
            .filter(
                company=company,
            )
            .count()
        )

    def round_tours_count(self, company: Company) -> int:
        return (
            Ride.round_tours.from_today_and_on()
            .filter(
                company=company,
            )
            .count()
        )
