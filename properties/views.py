from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .forms import PropertyForm
from profiles.models import LandlordProfile
from properties.models import Properties

# Create your views here.


def add_property(request):

    landlord = get_object_or_404(LandlordProfile, user=request.user)

    if request.method == 'POST':
        street_address = request.POST['street_address']
        properties = Properties.objects.all()
        the_property = properties.filter(street_address__exact=street_address)

        if the_property:
            messages.warning(request, f"{street_address} is already in \
                                    registered on the website and \
                                    cannot be registered twice.")
            property_form = PropertyForm()
        else:
            form_data = {
                    'landlord': landlord,
                    'street_address': street_address,
                    'house_name': request.POST['house_name'],
                    'post_code': request.POST['post_code'],
                    'no_of_bedrooms': request.POST['no_of_bedrooms'],
                    'activate': request.POST['activate-property'],
                }

            property_form = PropertyForm(form_data)

            if property_form.is_valid():
                property_form.save()
                property_form = PropertyForm()
                messages.success(request, f"{street_address} has been succesfuly registered and added to your list of properties.")

    else:
        property_form = PropertyForm()

    context = {
        'landlord': landlord,
        'property_form': property_form,
    }

    return render(request, 'add_property/add_property.html', context)


def remove_property(request, property_id):
    """
    A function that removes the property from the list and
    from the shopping cart if a service has been purchased
    for it.
    """
    cart = request.session.get('cart', {})
    this_property = get_object_or_404(Properties, pk=property_id)
    for properties in cart.values():
        for the_property in properties:
            if the_property == this_property.id:
                properties.remove(the_property)

    Properties.objects.filter(id=property_id).delete()
    request.session['cart'] = cart

    return redirect(reverse('profile'))


def activate_deactivate(request, property_id):

    this_property = get_object_or_404(Properties, pk=property_id)

    if this_property.activate:
        cart = request.session.get('cart', {})
        for properties in cart.values():
            for the_property in properties:
                if the_property == this_property.id:
                    properties.remove(the_property)
        request.session['cart'] = cart
        Properties.objects.filter(pk=property_id).update(activate=False)
    else:
        Properties.objects.filter(pk=property_id).update(activate=True)

    return redirect(reverse('profile'))

