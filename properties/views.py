from django.shortcuts import render, get_object_or_404, redirect, reverse
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
            print("there is already this property registered")
            property_form = PropertyForm()
        else:
            form_data = {
                    'landlord': landlord,
                    'street_address': street_address,
                    'house_name': request.POST['house_name'],
                    'post_code': request.POST['post_code'],
                    'no_of_bedrooms': request.POST['no_of_bedrooms'],
                }

            property_form = PropertyForm(form_data)

            if property_form.is_valid():
                property_form.save()

    else:
        property_form = PropertyForm()

    context = {
        'landlord': landlord,
        'property_form': property_form,
    }

    return render(request, 'add_property/add_property.html', context)

