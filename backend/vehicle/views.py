from django.views import generic


class VehicleView(generic.ListView):
    template_name = "vehicle.html"
    context_object_name = "vehicles"
