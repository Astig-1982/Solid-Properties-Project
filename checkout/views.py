from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem, OrderLineItemAnonym
from cart.contexts import cart_contents
from services.models import Services
from properties.models import Properties
from profiles.models import LandlordProfile
from profiles.forms import BillingForm

import stripe

# Create your views here.


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if request.user.is_authenticated:
            landlord = get_object_or_404(LandlordProfile, user=request.user)
        else:
            landlord = None

        form_data = {
            'landlord_profile': landlord,
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for service, properties_or_bedrooms in cart.items():
                service = get_object_or_404(Services, pk=service)
                for property_or_bedrooms in properties_or_bedrooms:
                    if request.user.is_authenticated:
                        the_property = get_object_or_404(Properties,
                                            pk=property_or_bedrooms)
                        order_line_item = OrderLineItem(
                            order=order,
                            service=service,
                            the_property=the_property,
                        )
                        request.session['save_info'] = \
                            'save-info' in request.POST
                    else:
                        order_line_item = OrderLineItemAnonym(
                            order=order,
                            service=service,
                            no_of_bedrooms=property_or_bedrooms,
                        )
                    order_line_item.save()
            return redirect(reverse('success_checkout',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There is was a problem with your form. \
                    Please check all fields and try again.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your shopping cart is empty.")
            return redirect(reverse('services'))

        current_cart = cart_contents(request)
        total = float(current_cart['grand_total'])
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            landlord = get_object_or_404(LandlordProfile, user=request.user)
            order_form = OrderForm(initial={
                    'full_name': landlord.default_full_name,
                    'email': landlord.user.email,
                    'phone_number': landlord.default_phone_number,
                    'country': landlord.default_country,
                    'postcode': landlord.default_postcode,
                    'town_or_city': landlord.default_town_or_city,
                    'street_address1': landlord.default_street_address1,
                    'street_address2': landlord.default_street_address2,
                })
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing.')

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

    return render(request, 'checkout/checkout.html', context)


def success_checkout(request, order_number):

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        if save_info:
            landlord = get_object_or_404(LandlordProfile, user=request.user)
            billing_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
            }
            billing_details_form = BillingForm(billing_data, instance=landlord)
            if billing_details_form.is_valid:
                billing_details_form.save()

    messages.success(request, f'Your order was succesful! \
                                We will send shortly a confirmation email to \
                                {order.email} with your order number \
                                 {order_number}.')

    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order': order,
    }

    return render(request, 'checkout/success_checkout.html', context)
