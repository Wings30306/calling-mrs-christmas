from django.conf.urls import url
from .views import checkout_view

app_name = "checkout"
urlpatterns = [
    url("", checkout_view, name="checkout")
]
