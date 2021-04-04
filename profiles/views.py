from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import LandlordProfile
from checkout.models import Order
from .forms import BillingForm


# Create your views here.


@login_required
def landlord_profile(request):
    """
    This view displays user's profile
    and its list of properties and orders.
    """
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
    """
    This view displays user's past orders.
    """
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


@login_required
def billing_details(request):
    """
    This view displays and updates user's billing details.
    """
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


def personalised_shopping_profile(request):
    """
    This view displays personalised shopping page
    if it's accessed from the profile page.
    """
    context = {
        'from_profile': True,
    }

    return render(request, 'home/personalised.html', context)


