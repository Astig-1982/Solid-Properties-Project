from django.shortcuts import render, get_object_or_404
from .models import LandlordProfile

# Create your views here.


def landlord_profile(request):

    landlord = get_object_or_404(LandlordProfile, user=request.user)

    context = {
        'landlord': landlord
    }

    return render(request, 'profiles/profile.html', context)



