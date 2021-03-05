from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import LandlordProfile
from properties.models import Properties
from checkout.models import Order
from .forms import BillingForm

# Create your views here.


def landlord_profile(request):

    landlord = get_object_or_404(LandlordProfile, user=request.user)
    all_properties = landlord.properties.all()
    orders = landlord.orders.all()
    properties = all_properties.order_by('street_address')
    properties_count = all_properties.count()

    context = {
        'landlord': landlord,
        'properties': properties,
        'properties_count': properties_count,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/success_checkout.html', context)


def billing_details(request):

    landlord = get_object_or_404(LandlordProfile, user=request.user)

    if request.method == 'POST':
        billing_form = BillingForm(request.POST, instance=landlord)
        if billing_form.is_valid():
            billing_form.save()
            messages.success(request, 'Your billing details \
                                    have been updated succesfuly.')

    billing_form = BillingForm(instance=landlord)

    context = {
        'landlord': landlord,
        'billing_form': billing_form,
    }

    return render(request, 'profiles/billing_details.html', context)


