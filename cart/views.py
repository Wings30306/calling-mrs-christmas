from django.shortcuts import render, redirect, reverse
from .contexts import cart_contents
from .models import Cart

# Create your views here.
def helper_check_user_cart(request):
    """function to check whether authenticated user has cart"""
    if request.user.is_authenticated:
        try:
            cart_instance = Cart.objects.get(user=request.user)
            print(cart_instance)
            cart = cart_instance.cart
            request.session["cart"] = cart
        except Cart.DoesNotExist:
            cart = {"cart_items": [], "total": 0, "count": 0}
        finally:
            request.session["cart"] = cart
    else:
        cart = request.session["cart"]
    return cart

def view_cart(request):
    """ A view that renders the cart contents page """
    template_name = "cart/cart.html"
    return render(request, template_name=template_name)


def add_to_cart(request, primary_key):
    """Add a quantity of the specified product to the cart"""
    cart = helper_check_user_cart(request)
    quantity = request.POST.get("quantity")
    new_cart_item = {"primary_key": primary_key, "quantity": quantity}
    print(new_cart_item)
    index = 0
    for item in cart["cart_items"]:
        if item["primary_key"] == new_cart_item["primary_key"]:
            if item["quantity"] == "":
                quantity = 0
            else:
                quantity = int(item["quantity"])
            quantity += int(new_cart_item["quantity"])
            request.session["cart"]["cart_items"][index]["quantity"] = quantity
            cart_contents(request)
            return redirect(reverse('cart:view_cart'))
        index += 1
    cart['cart_items'].append(new_cart_item)
    if request.user.is_authenticated:
        Cart.objects.filter(user=request.user).update(
            user=request.user,
            cart=request.session["cart"])
    cart_contents(request)
    return redirect(reverse('cart:view_cart'))


def adjust_cart(request, primary_key):
    """Adjust the quantity of the specified product to the specified amount"""
    cart = helper_check_user_cart(request)
    quantity = request.POST.get("quantity")
    new_cart_item = {"primary_key": primary_key, "quantity": quantity}
    print(new_cart_item)
    index = 0
    for item in cart["cart_items"]:
        if item["primary_key"] == new_cart_item["primary_key"]:
            if int(new_cart_item["quantity"]) == 0:
                request.session["cart"]["cart_items"].pop(index)
            else:
                quantity = new_cart_item["quantity"]
                request.session["cart"]["cart_items"][index]["quantity"] = quantity
        index += 1
    cart_contents(request)
    if request.user.is_authenticated:
        Cart.objects.filter(user=request.user).update(cart=request.session["cart"])
    return redirect(reverse('cart:view_cart'))
