from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, "cart.html")

def add_to_cart(request, primary_key):
    """ Add a quantity of the specified product to the cart """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[primary_key] = cart.get(primary_key, quantity)
    request.session['cart'] = cart
    return redirect(reverse('services:services_list'))

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
