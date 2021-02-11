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


