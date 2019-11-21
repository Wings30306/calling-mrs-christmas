from django.contrib import admin
from django.urls import path
from .views import index_page

app_name = "about"
urlpatterns = [
    path('', index_page, name="index"),
]