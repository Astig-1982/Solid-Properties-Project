from django.conf import settings
from django.shortcuts import get_object_or_404, render
from services.models import Services


def cart_contents(request):

    cart_items = []
    cart = request.session.get('cart', {})
    grand_total = []

    if request.user.is_authenticated:
        for service, addresses in cart.items():
            total = []
            list_addresses = []
            service = get_object_or_404(Services, pk=service)
            for address in addresses:
                for key_address, no_of_bedrooms in address.items():
                    total_cost = no_of_bedrooms * float(service.price)
                    total.append(total_cost)
                    list_addresses.append({
                        "address": key_address,
                        "no_of_bedrooms": no_of_bedrooms,
                        "total_cost": total_cost,
                    })
            grand_total.append(sum(total))
            cart_items.append({
                "service": service,
                "properties": list_addresses,
            })

    grand_total = sum(grand_total)

    context = {
        "cart_items": cart_items,
        "grand_total": grand_total,
    }

    return context

