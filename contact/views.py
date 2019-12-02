from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Location

# Create your views here.
class LocationListView(ListView):
    queryset = Location.objects.all()

class LocationDetailView(DetailView):
    model = Location

class LocationCreateView(CreateView):
    model = Location

class LocationUpdateView(UpdateView):
    model = Location

class LocationDeleteView(DeleteView):
    model = Location