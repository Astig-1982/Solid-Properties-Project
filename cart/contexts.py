from django.shortcuts import get_object_or_404
from services.models import Services
from properties.models import Properties


def cart_contents(request):

    cart_items = []
    cart = request.session.get('cart', {})
    count_items = []
    grand_total = 0
    grand_total = []

    for service, properties_or_bedrooms in cart.items():
        total = []
        list_properties_or_bedrooms = []
        service = get_object_or_404(Services, pk=service)
        for property_or_bedrooms in properties_or_bedrooms:
            if request.user.is_authenticated:
                the_property = get_object_or_404(Properties,
                                                 pk=property_or_bedrooms)
                if service.price_variation:
                    total_cost = the_property.no_of_bedrooms * service.price
                else:
                    total_cost = service.price
                total.append(total_cost)
                count_items.append(the_property)
                list_properties_or_bedrooms.append({
                    'property': the_property,
                    'total_cost': total_cost,
                })
            else:
                if service.price_variation:
                    total_cost = property_or_bedrooms * service.price
                else:
                    total_cost = service.price
                total.append(total_cost)
                count_items.append(property_or_bedrooms)
                list_properties_or_bedrooms.append({
                    'no_of_bedrooms': property_or_bedrooms,
                    'total_cost': total_cost,
                })

        grand_total.append(sum(total))
        total = format(sum(total), '.2f')
        cart_items.append({
            'service': service,
            'properties_or_bedrooms': list_properties_or_bedrooms,
            'total_for_all_properties': total,
        })

    # calculate the number of items in the cart
    if cart_items:
        count_cart = len(count_items)
    else:
        count_cart = 0

    grand_total = format(sum(grand_total), '.2f')
    print(cart_items)

    context = {
            "cart_items": cart_items,
            "grand_total": grand_total,
            "count_cart": count_cart,
        }

    return context
