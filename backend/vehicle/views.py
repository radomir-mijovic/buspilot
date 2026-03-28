from django.views import generic

from .forms import VehicleCreateForm
from .models import Vehicle


class VehicleView(generic.ListView):
    template_name = "vehicle.html"
    context_object_name = "vehicles"

    def get_queryset(self):
        return Vehicle.objects.filter(
            company=self.request.user.company,
        ).select_related("company")


class VehicleCreateView(generic.CreateView):
    model = Vehicle
    form_class = VehicleCreateForm
