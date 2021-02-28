from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import LandlordProfile
from properties.models import Properties
from checkout.models import Order

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

    return redirect(reverse('success_checkout',
                            args=[order.order_number]))



