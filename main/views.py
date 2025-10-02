from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def destinations(request):
    all_destinations = Destination.objects.all()
    return render(request, "destinations.html", {"destinations": all_destinations})
