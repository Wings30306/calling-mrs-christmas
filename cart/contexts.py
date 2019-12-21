from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    cart = {}
    cart_items = []
    total = 0
    count = 0
    for primary_key, quantity in cart.items():
        service = get_object_or_404(Service, pk=primary_key)
        total += quantity * service.price
        count += quantity
        cart_items.append({"service": service, "quantity": quantity})
    cart = {"cart_items": cart_items, "total": total, "count": count}
    print(cart)
    return cart
