from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView)
from .views import logout, login, register, user_profile, edit_profile

app_name = "accounts"
urlpatterns = [
    path('logout', logout, name="logout"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('profile', user_profile, name="profile"),
    path('profile/edit', edit_profile, name="edit_profile"),
    path('password-reset/', PasswordResetView.as_view(success_url=reverse_lazy(
        'accounts:password_reset_done')), name="password_reset"),
    path('password-reset/done', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:login')), name='password_reset_confirm'),
]
