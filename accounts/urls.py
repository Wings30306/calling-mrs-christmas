from django.contrib import admin
from django.urls import path, include
from .views import logout, login, register, user_profile, edit_profile

app_name = "accounts"
urlpatterns = [
    path('logout', logout, name="logout"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('profile', user_profile, name="profile"),
    path('profile/edit', edit_profile, name="edit_profile"),
    path('password-reset/', include('accounts.urls_reset'))
]