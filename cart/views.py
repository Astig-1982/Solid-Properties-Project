from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
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
            messages.success(request, f"You have added {service.name} for {the_property.street_address} to your shopping cart.")
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
        messages.success(request, f"You have added {service.name} to your shopping cart.")
        print(request.session['cart'])

    return redirect(redirect_url)


def remove_from_cart(request, service_id):

    cart = request.session.get('cart', {})
    service = get_object_or_404(Services, pk=service_id)
    property_id = None
    no_of_bedrooms = None
    if 'property_id' in request.POST:  # if the user is logged in
        property_id = request.POST['property_id']
    elif 'no_of_bedrooms' in request.POST:  # if the user is not logged in
        no_of_bedrooms = request.POST['no_of_bedrooms']
 
    if property_id:
        this_property = get_object_or_404(Properties, pk=property_id)
        for the_property in cart[service_id]:
            if the_property == this_property.id:
                cart[service_id].remove(the_property)
                messages.success(request, f"{service.name} for {this_property.street_address} has been removed from your shopping cart.")
        if not cart[service_id]:
            cart.pop(service_id)
            messages.success(request, f"{service.name} has been removed from your shopping cart.")
    elif no_of_bedrooms:
        for bedrooms in cart[service_id]:
            if int(bedrooms) == int(no_of_bedrooms):
                cart[service_id].remove(bedrooms)
                messages.success(request, f"{service.name} for {bedrooms} bedrooms has been removed from your shopping cart.")
        if not cart[service_id]:
            cart.pop(service_id)
            messages.success(request, f"{service.name} has been removed from your shopping cart.")
    else:
        cart.pop(service_id)
        messages.success(request, f"{service.name} has been removed from your shopping cart.")

    request.session['cart'] = cart

    context = {}

    return render(request, 'cart/cart.html', context)


