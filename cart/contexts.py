from django.shortcuts import get_object_or_404
from services.models import Service
from .models import Cart


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    if request.user.is_authenticated:
        try:
            cart_instance = Cart.objects.get(user=request.user)
            print(cart_instance)
            if cart_instance.cart == {}:
                empty_cart = {"cart_items": [], "total": 0, "count": 0}
                Cart.objects.filter(user=request.user).update(
                    user=request.user,
                    cart=empty_cart)
                cart_instance = Cart.objects.get(user=request.user)
            cart = cart_instance.cart
            request.session["cart"] = cart
        except Cart.DoesNotExist:
            if request.session["cart"]:
                cart = request.session["cart"]
            else:
                cart = {"cart_items": [], "total": 0, "count": 0}
        finally:
            request.session["cart"] = cart
    cart_items = []
    total = 0
    count = 0
    cart = request.session.get(
        "cart", {"cart_items": cart_items, "total": total, "count": count})
    print(cart)
    if len(cart['cart_items']) > 0:
        index = 0
        for item in cart['cart_items']:
            primary_key = item['primary_key']
            if item['quantity'] == '':
                quantity = 0
            else:
                quantity = int(item['quantity'])
            if quantity == 0:
                cart['cart_items'].pop(index)
            else:
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
            index += 1
        cart = {"cart_items": cart_items, "total": total, "count": count}
    else:
        cart = {"cart_items": [], "total": 0, "count": 0}
    
    request.session["cart"] = cart
    return cart
