from django.shortcuts import render


def expired_documents(request):
    template = "expiring-documents.html"
    return render(request, template, {})
