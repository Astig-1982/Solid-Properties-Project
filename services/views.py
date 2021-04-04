from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Services, Category
from profiles.models import LandlordProfile

# Create your views here.


def all_services(request):
    """
    This view displays and sorts services
    """
    services = Services.objects.all()
    categories = Category.objects.all()
    query = None
    category = None
    sort = None
    direction = None
    current_category = 'services'

    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET['sort']

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort = f'-{sort}'

            services = services.order_by(sort)

        if 'category' in request.GET:
            category = request.GET['category']
            services = services.filter(category__name__exact=category)
            current = get_object_or_404(Category, name=category)
            current_category = current.friendly_name

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.warning(request, "No entry has been dedected")
                return redirect(reverse('services'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query) | \
                Q(short_description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'search': query,
        'categories': categories,
        'current_category': current_category,
    }

    return render(request, 'services/services.html', context)


def detailed_service(request, service_id):
    """
    This view displays a specific service in detail
    """
    service = get_object_or_404(Services, pk=service_id)
    if request.user.is_authenticated:
        landlord = get_object_or_404(LandlordProfile, user=request.user)
        properties = landlord.properties.all()
        context = {
            'service': service,
            'landlord': landlord,
            'properties': properties,
        }
        return render(request, 'services/detailed_service.html', context)

    context = {
            'service': service,
        }

    return render(request, 'services/detailed_service.html', context)








