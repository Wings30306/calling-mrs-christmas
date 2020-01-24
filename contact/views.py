from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Location
from .forms import LocationModelForm

# Create your views here.
class LocationListView(ListView):
    queryset = Location.objects.all()

class LocationDetailView(DetailView):
    model = Location

class LocationCreateView(CreateView):
    template_name = 'contact/location_create.html'
    form_class = LocationModelForm

class LocationUpdateView(UpdateView):
    template_name = 'contact/location_create.html'
    form_class = LocationModelForm
    model = Location

class LocationDeleteView(DeleteView):
    model = Location
