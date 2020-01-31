"""callingmrschristmas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView
from about.views import index_view
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('accounts/password-reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:login'), template_name="password_reset_confirm.html"),
         name='password_reset_confirm'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
