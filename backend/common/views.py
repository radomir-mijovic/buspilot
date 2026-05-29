from django.shortcuts import render


def expiring_documents(request):
    template = "expiring-documents.html"
    return render(request, template, {})


def expired_documents(request):
    template = "expired-documents.html"
    return render(request, template, {})


def index(request):
    temlate = "index.html"
    return render(request, temlate, {})
