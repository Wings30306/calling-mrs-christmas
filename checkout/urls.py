from django.conf.urls import url
from .views import checkout

urlpatterns = [
    url("", checkout, name="checkout")
]
