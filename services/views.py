from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Service

# Create your views here.
class ServiceListView(ListView):
    queryset = Service.objects.all()

class ServiceDetailView(DetailView):
    model = Service