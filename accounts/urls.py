from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView)
from .views import logout, login, register, user_profile

app_name = "accounts"
urlpatterns = [
    path('logout', logout, name="logout"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('profile', user_profile, name="profile"),
    path('password-reset/', PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_done'),
        template_name="password_reset_form.html"),
         name="password_reset"),
    path('password-reset/done', PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"),
         name='password_reset_done'),
]
