from django.contrib import admin
from django.urls import path
from .views import logout, login, register, profile, edit_profile

app_name = "accounts"
urlpatterns = [
    path('logout', logout, name="logout"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('<slug:username>', profile, name="profile"),
    path('<slug:username>/edit', edit_profile, name="edit_profile"),
]