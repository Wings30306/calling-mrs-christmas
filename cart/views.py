from django.shortcuts import render, redirect, reverse
from .contexts import cart_contents

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """
    template_name = "cart/cart.html"
    return render(request, template_name=template_name)


def add_to_cart(request, primary_key):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get("quantity"))

    new_cart_item = (primary_key, quantity)
    print(new_cart_item)
    request.session["cart"] = cart_contents(request)
    cart = request.session.get("cart")
    print(cart)
    return redirect(reverse('cart:view_cart'))


def adjust_cart(request, primary_key):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[primary_key] = quantity
    else:
        cart.pop(primary_key)

    request.session['cart'] = cart
    return redirect('view_cart')
