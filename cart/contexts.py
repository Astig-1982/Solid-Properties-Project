from django.conf import settings
from django.shortcuts import get_object_or_404, render
from services.models import Services


def cart_contents(request):

    cart_items = []
    cart = request.session.get('cart', {})
    grand_total = 0

    if request.user.is_authenticated:
        grand_total = []
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
            total = sum(total)
            cart_items.append({
                "service": service,
                "properties": list_addresses,
                "total_for_all_properties": total,
            })

    else:
        grand_total = []
        for service, bedrooms in cart.items():
            list_bedrooms = []
            service = get_object_or_404(Services, pk=service)
            for no_of_bedrooms in bedrooms:
                total_cost = no_of_bedrooms * float(service.price)
                grand_total.append(total_cost)
                list_bedrooms.append(no_of_bedrooms)
            cart_items.append({
                "service": service,
                "list_bedrooms": list_bedrooms,
            })

    grand_total = sum(grand_total)

    context = {
            "cart_items": cart_items,
            "grand_total": grand_total,
        }

    print(cart_items)

    return context

