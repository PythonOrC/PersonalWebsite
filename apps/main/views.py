from django.http import Http404
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def general(request, slug):
    return render(request, f"{slug}.html")
