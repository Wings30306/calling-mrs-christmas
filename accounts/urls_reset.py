from django.contrib import admin
from django.conf.urls import url
from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('', PasswordResetView.as_view(), {'post_reset_redirect': reverse_lazy('password_reset_done')}, name="password_reset"),
    path('done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('?<uidb64>[0-9A-Za-z]+)-<token>).+', PasswordResetConfirmView.as_view(), {'post_reset_confirm': reverse_lazy('accounts:password_reset_complete')}, name='password_reset_confirm'),
    path('complete', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
