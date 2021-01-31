from django.conf import settings
from django.shortcuts import get_object_or_404, render
from services.models import Services


def cart_contents(request):

    cart_items = []
    cart = request.session.get('cart', {})

    for service, addresses in cart.items():
        total = []
        for address in addresses:
            for key in address:
                total_price = address[key] * 2
                total.append(total_price)
        cart_items.append({
            service: addresses,
            "total_for_this_service": sum(total),
        })

    context = {
        'cart_items': cart_items,
    }

    return context


