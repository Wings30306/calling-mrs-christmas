from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
import stripe
from services.models import Service
from checkout.models import OrderLineItem
from checkout.forms import OrderForm, MakePaymentForm
from cart.models import Cart


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


def checkout_view(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        order_dict = order_form.__dict__
        payment_form = MakePaymentForm(request.POST)
        save_details = request.POST.get("save-details")
        if save_details == "on":
            phone = order_dict["data"]["phone_number"]
            street1 = order_dict["data"]["street_address1"]
            street2 = order_dict["data"]["street_address2"]
            town = order_dict["data"]["town_or_city"]
            postcode = order_dict["data"]["postcode"]
            county = order_dict["data"]["county"]
            country = order_dict["data"]["country"]
            print(phone, street1, street2, town, postcode, county, country)
        if order_form.is_valid() and payment_form.is_valid():
            cart = request.session.get('cart', {})
            total = cart["total"]
            customer = None
            try:
                customer = stripe.Charge.create(
                    amount=int(total),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                return redirect(reverse("checkout"))

            if customer is not None:
                if customer.paid:
                    messages.success(request, "You have successfully paid.")
                    order = order_form.save(commit=False)
                    order.date = timezone.now()
                    order.save()
                    for item in cart["cart_items"]:
                        service = get_object_or_404(
                            Service, pk=item["primary_key"])
                        quantity = item["quantity"]
                        total += quantity * service.price_in_p
                        order_line_item = OrderLineItem(
                            order=order,
                            service=service,
                            quantity=quantity
                        )
                        order_line_item.save()

                    request.session['cart'] = {
                        "cart_items": [], "total": 0, "count": 0}
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
