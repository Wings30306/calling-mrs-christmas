from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    cart_items = []
    total = 0
    count = 0
    cart = request.session.get(
        "cart", {"cart_items": cart_items, "total": total, "count": count})
    if len(cart['cart_items']) > 0:
        for item in cart['cart_items']:
            primary_key = item['primary_key']
            quantity = int(item['quantity'])
            service = get_object_or_404(Service, pk=primary_key)
            price = int(service.price)
            total += quantity * price
            count += quantity
            cart_items.append({"primary_key": primary_key, "quantity": quantity})
    cart = {"cart_items": cart_items, "total": total, "count": count}
    request.session["cart"] = cart
    return cart
