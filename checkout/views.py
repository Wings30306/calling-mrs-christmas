from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from services.models import Service
from checkout.models import OrderLineItem
from checkout.forms import OrderForm, MakePaymentForm
from cart.models import Cart
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


def checkout_view(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        print(payment_form)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for item in cart["cart_items"]:
                service = get_object_or_404(Service, pk=item["primary_key"])
                quantity = item["quantity"]
                total += quantity * service.price_in_p
                order_line_item = OrderLineItem(
                    order=order,
                    service=service,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid.")
                request.session['cart'] = {"cart_items": [], "total": 0, "count": 0}
                if request.user.is_authenticated:
                    Cart.objects.filter(user=request.user).update(
                        user=request.user,
                        cart=request.session["cart"])
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    return render(request, "checkout.html", {"payment_form": payment_form,
                                             "order_form": order_form,
                                             "publishable": settings.STRIPE_PUBLISHABLE})
