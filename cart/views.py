from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from services.models import Services
from properties.models import Properties

# Create your views here.


def view_cart(request):

    context = {}

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, service_id):

    service = get_object_or_404(Services, pk=service_id)
    street_address = request.POST.get("street_address")
    redirect_url = request.POST.get('redirect_url')

    if request.user.is_authenticated:
        the_property = get_object_or_404(Properties, street_address=street_address)
        if street_address:
            cart = request.session.get('cart', {})
            cart.setdefault(service_id, [])
            cart[service_id].append(the_property.id)
            request.session['cart'] = cart
            print(request.session['cart'])
        else:
            print("No value")
            return redirect(redirect_url)
    else:
        if service.price_variation:
            no_of_bedrooms = int(request.POST.get('no_of_bedrooms'))
        else:
            no_of_bedrooms = 1
        cart = request.session.get('cart', {})
        cart.setdefault(service_id, [])
        cart[service_id].append(no_of_bedrooms)
        request.session['cart'] = cart
        print(request.session['cart'])

    return redirect(redirect_url)


def remove_from_cart(request, service_id):

    cart = request.session.get('cart', {})
    cart.pop(service_id)
    request.session['cart'] = cart

    context = {}

    return render(request, 'cart/cart.html', context)


def remove_address(request, service_id):

    cart = request.session.get('cart', {})
    property_id = request.POST['property_id']
    this_property = get_object_or_404(Properties, pk=property_id)

    for the_property in cart[service_id]:
        if the_property == this_property.id:
            cart[service_id].remove(the_property)

    request.session['cart'] = cart

    context = {}

    return render(request, 'cart/cart.html', context)
