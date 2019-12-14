from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Service, ServiceCategory

# Create your views here.


class ServiceCategoryListView(ListView):
    """Show all the service categories and their description"""
    template_name = 'services/service-categories-list.html'
    queryset = ServiceCategory.objects.all()


def service_list_by_category_view(request, category):
    template_name = 'services/service-list-by-category.html'
    obj = ServiceCategory.objects.get(name=category)
    queryset = Service.objects.filter(category=obj.pk)
    context = {
        "obj": obj,
        "queryset": queryset
    }
    return render(request, template_name=template_name, context=context)


class ServiceDetailView(DetailView):
    model = Service
