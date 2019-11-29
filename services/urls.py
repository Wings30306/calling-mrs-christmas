from django.contrib import admin
from django.urls import path
from .views import services_list_view, services_detail_view

app_name = "services"
urlpatterns = [
    path('', services_list_view, name="services_list"),
    path('<int:id>', services_detail_view, name="service_detail"),
]