from django.shortcuts import render


def request_demo(request):
    template = "request-demo.html"
    return render(request, template, {})
