from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from services.models import Services

# Create your views here.


def view_cart(request):

    context = {}

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, service_id):

    service = get_object_or_404(Services, pk=service_id)
    street_address = request.POST.get("street_address")
    redirect_url = request.POST.get('redirect_url')

    if service.price_variation:
        no_of_bedrooms = int(request.POST.get('no_of_bedrooms'))
    else:
        no_of_bedrooms = 1

    if request.user.is_authenticated:
        if street_address:
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

    else:
        cart = request.session.get('cart', {})
        cart.setdefault(service_id, [])
        cart[service_id].append(no_of_bedrooms)
        request.session['cart'] = cart
        print(request.session['cart'])

    return redirect(redirect_url)


def remove_from_cart(request, service_id):

    property_address = None
    cart = request.session.get('cart', {})
    if 'property_address' in request.POST:
        property_address = request.POST['property_address']

    if property_address:
        for address in cart[service_id]:
            for address_key in address.keys():
                if address_key == property_address:
                    dict_address = address
        dict_address.clear()
        if all(not d for d in cart[service_id]):
            cart.pop(service_id)
    else:
        cart.pop(service_id)
    request.session['cart'] = cart

    context = {}

    return render(request, 'cart/cart.html', context)



