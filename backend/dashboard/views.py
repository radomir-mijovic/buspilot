from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from ride.models import Ride


@login_required
def dashboard(request):
    user = request.user
    template = loader.get_template("dashboard.html")

    lines = Ride.lines.today(company=user.company)
    transfers = Ride.transfers.today(company=user.company)
    excursions = Ride.excursions.today(company=user.company)

    context = {
        "user": user,
        "lines": lines,
        "transfers": transfers,
        "excursions": excursions,
    }
    return HttpResponse(template.render(context, request))
