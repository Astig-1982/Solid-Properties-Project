from django.shortcuts import get_object_or_404
from services.models import Services
from properties.models import Properties


def cart_contents(request):

    cart_items = []
    cart = request.session.get('cart', {})
    grand_total = 0

    grand_total = []
    for service, addresses_or_bedrooms in cart.items():
        total = []
        list_addresses_or_bedrooms = []
        service = get_object_or_404(Services, pk=service)
        for address_or_no_of_bedrooms in addresses_or_bedrooms:
            if request.user.is_authenticated:
                for key_address, no_of_bedrooms in address_or_no_of_bedrooms.items():
                    the_property = get_object_or_404(Properties, street_address=key_address)
                    total_cost = no_of_bedrooms * float(service.price)
                    total.append(total_cost)
                    list_addresses_or_bedrooms.append({
                        "the_property": the_property,
                        "total_cost": format(total_cost, '.2f'),
                    })
            else:
                total_cost = address_or_no_of_bedrooms * float(service.price)
                total.append(total_cost)
                list_addresses_or_bedrooms.append({
                    "no_of_bedrooms": address_or_no_of_bedrooms,
                    "total_cost": format(total_cost, '.2f'),
                })
        grand_total.append(sum(total))
        total = format(sum(total), '.2f')
        cart_items.append({
            "service": service,
            "properties_or_bedrooms": list_addresses_or_bedrooms,
            "total_for_all_properties": total,
        })

    grand_total = format(sum(grand_total), '.2f')

    context = {
            "cart_items": cart_items,
            "grand_total": grand_total,
        }

    return context
