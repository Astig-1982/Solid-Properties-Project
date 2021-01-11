from django.shortcuts import render, get_object_or_404
from .models import Services

# Create your views here.


def all_services(request):

    services = Services.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def detailed_service(request, service_id):

    service = get_object_or_404(Services, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/detailed_service.html', context)


