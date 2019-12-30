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
    quantity = request.POST.get("quantity")
    new_cart_item = {"primary_key": primary_key, "quantity": quantity}
    print(new_cart_item)
    for item in cart["cart_items"]:
        index = 0
        if item["primary_key"] == new_cart_item["primary_key"]:
            quantity = int(item["quantity"])
            quantity += int(new_cart_item["quantity"])
            request.session["cart"]["cart_items"][index]["quantity"] = quantity
            cart_contents(request)
            index += 1
            return redirect(reverse('cart:view_cart'))
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
