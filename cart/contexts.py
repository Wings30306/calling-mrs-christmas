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
            quantity = item['quantity']
            service = get_object_or_404(Service, pk=primary_key)
            price = service.price_in_p
            title = service.title
            img = service.img_name
            alt = service.img_alt
            url = service.get_absolute_url()
            description = service.brief_description
            item_total = quantity * price
            total += item_total
            count += quantity
            cart_items.append({"primary_key": primary_key,
                               "title": title,
                               "price": price,
                               "img": img,
                               "alt": alt,
                               "url": url,
                               "quantity": quantity,
                               "description": description,
                               "item_total": item_total
                               })
    cart = {"cart_items": cart_items, "total": total, "count": count}
    request.session["cart"] = cart
    return cart
