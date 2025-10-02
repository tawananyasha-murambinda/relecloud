from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Destination
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .forms import InquiryForm

def hello(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


class DestinationListView(ListView):
    model = Destination
    template_name = "destinations.html"

class DestinationDetailView(DetailView):
    model = Destination
    template_name = "destination_detail.html"

def inquiry(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        form = InquiryForm()
    return render(request, 'inquiry.html', {'form': form})