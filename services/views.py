from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Service

# Create your views here.
class ServiceListView(ListView):
    queryset = Service.objects.all()

def services_detail_view(request, *args, **kwargs):
    return render(request, "services_detail.html")