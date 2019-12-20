from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart

app_name = "cart"
urlpatterns = [
    path('', view_cart, name="view_cart"),
    path('add/<int:primary_key>', add_to_cart, name="add_to_cart"),
    path('adjust/<int:primary_key>', adjust_cart, name="adjust_cart")
]
