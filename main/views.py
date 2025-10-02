from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Destination, Cruise
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
    context_object_name = "destinations"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cruises'] = Cruise.objects.all()
        return context

class DestinationDetailView(DetailView):
    model = Destination
    template_name = "destination_detail.html"
    context_object_name = "destination"

def inquiry(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InquiryForm()

    return render(request, 'inquiry.html', {'form': form})
