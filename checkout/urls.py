from django.conf.urls import url
from .views import checkout_view

urlpatterns = [
    url("", checkout_view, name="checkout")
]
