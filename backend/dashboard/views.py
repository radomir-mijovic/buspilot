from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader


@login_required
def dashboard(request):
    user = request.user
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render({"user": user}, request))
