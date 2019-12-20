from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    count = 0
    for primary_key, quantity in cart_items:
        service = get_object_or_404(Service, pk=primary_key)
        total += quantity * service.price
        count += quantity
        cart_items.append({"id": id, "quantity": quantity})
    return {"cart_items": cart_items, "total": total, "product_count": count}
