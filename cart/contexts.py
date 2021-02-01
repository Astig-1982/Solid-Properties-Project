from django.conf import settings
from django.shortcuts import get_object_or_404, render
from services.models import Services
from properties.models import Properties


def cart_contents(request):

    cart_items = []
    cart = request.session.get('cart', {})

    for service_id, addresses in cart.items():
        total = []
        service = get_object_or_404(Services, pk=service_id)
        for address in addresses:
            for dict_address in address:
                total_price = address[dict_address] * float(service.price)
                total.append(total_price)
        cart_items.append({
            service: addresses,
            "total_for_this_service": sum(total),
        })

    context = {
        'cart_items': cart_items,
    }

    return context


