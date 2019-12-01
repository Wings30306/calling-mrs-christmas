from django.contrib import admin
from django.urls import path
from .views import LocationListView

app_name = "contact"
urlpatterns = [
    path('', LocationListView.as_view(), name="contact"),

]