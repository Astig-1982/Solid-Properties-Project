from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Services

# Create your views here.


def all_services(request):

    services = Services.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No entry has been dedected")
                return redirect(reverse('services'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(short_description__icontains=query)
            services = services.filter(queries)

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


