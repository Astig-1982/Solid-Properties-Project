from django.shortcuts import render
from .models import Services

# Create your views here.


def all_services(request):

    services = Services.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


