from django.shortcuts import render, get_object_or_404
from .models import LandlordProfile
from properties.models import Properties

# Create your views here.


def landlord_profile(request):

    landlord = get_object_or_404(LandlordProfile, user=request.user)
    all_properties = landlord.properties.all()
    properties = all_properties.order_by('street_address')
    properties_count = all_properties.count()

    context = {
        'landlord': landlord,
        'properties': properties,
        'properties_count': properties_count,
    }

    return render(request, 'profiles/profile.html', context)



