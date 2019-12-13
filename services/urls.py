from django.contrib import admin
from django.urls import path
from .views import ServiceCategoryListView, ServiceDetailView

app_name = "services"
urlpatterns = [
    path('', ServiceCategoryListView.as_view(), name="services_list"),
    path('<int:pk>', ServiceDetailView.as_view(), name="service_detail"),
]