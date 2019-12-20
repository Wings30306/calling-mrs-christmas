from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import Service, ServiceCategory

# Create your views here.


class ServiceCategoryListView(ListView):
    """Show all the service categories and their description"""
    template_name = 'services/service-categories-list.html'
    queryset = ServiceCategory.objects.all()


def service_list_by_category_view(request, category):
    """Shows services for a chosen category.
    If url doesn't link to existing category, return user to categories list"""
    template_name = 'services/service-list-by-category.html'
    try:
        obj = ServiceCategory.objects.get(name=category)
        queryset = Service.objects.filter(category=obj.pk)
        context = {
            "obj": obj,
            "queryset": queryset
        }
    except ServiceCategory.DoesNotExist:
        messages.error(request, 'No category named <em>' + category + '</em>.')
        return redirect("services:services_list")
    return render(request, template_name=template_name, context=context)


def service_detail_view(request, primary_key):
    """Shows details for a specific service"""
    template_name = 'services/service-detail.html'
    try:
        obj = Service.objects.get(pk=primary_key)
        context = {
            "object": obj
        }
    except ServiceCategory.DoesNotExist:
        messages.error(request, 'No service with this id: ' + primary_key + '</em>.')
        return redirect("services:services_list")
    return render(request, template_name=template_name, context=context)
