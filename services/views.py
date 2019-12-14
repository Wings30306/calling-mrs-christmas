from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Service, ServiceCategory

# Create your views here.
class ServiceCategoryListView(ListView):
    template_name = 'services/service-categories-list.html'
    queryset = ServiceCategory.objects.all()

class ServiceDetailView(DetailView):
    model = Service