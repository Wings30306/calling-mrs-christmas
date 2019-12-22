from django.shortcuts import render, redirect, reverse
from .contexts import cart_contents

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """
    template_name = "cart/cart.html"
    return render(request, template_name=template_name)


def add_to_cart(request, primary_key):
    """Add a quantity of the specified product to the cart"""
    cart = request.session.get("cart")
    print(cart)
    quantity = request.POST.get("quantity")
    print(quantity)
    print(primary_key)

    new_cart_item = {"primary_key": primary_key, "quantity": quantity}
    print(new_cart_item)
    cart['cart_items'].append(new_cart_item)
    cart_contents(request)
    return redirect(reverse('cart:view_cart'))


def adjust_cart(request, primary_key):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = request.POST.get('quantity')
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[primary_key] = quantity
    else:
        cart.pop(primary_key)

    request.session['cart'] = cart
    return redirect('view_cart')
