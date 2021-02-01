from django.shortcuts import render, get_object_or_404, redirect
from services.models import Services

# Create your views here.


def view_cart(request):

    context = {}

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, service_id):

    service = get_object_or_404(Services, pk=service_id)
    street_address = request.POST.get("street_address")
    redirect_url = request.POST.get('redirect_url')

    if street_address:
        if service.price_variation:
            no_of_bedrooms = int(request.POST.get('no_of_bedrooms'))
        else:
            no_of_bedrooms = 1

        cart = request.session.get('cart', {})
        cart.setdefault(service_id, [])
        street_bedrooms = {}
        street_bedrooms[street_address] = no_of_bedrooms
        street_bedrooms_copy = street_bedrooms.copy()
        cart[service_id].append(street_bedrooms_copy)

        request.session['cart'] = cart
        print(request.session['cart'])
    else:
        print("No value.")
        return redirect(redirect_url)

    return redirect(redirect_url)




