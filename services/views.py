from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Services, Category

# Create your views here.


def all_services(request):

    services = Services.objects.all()
    categories = Category.objects.all()
    query = None
    category = None

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

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No entry has been dedected")
                return redirect(reverse('services'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(short_description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'search': query,
        'categories': categories,
    }

    return render(request, 'services/services.html', context)


def detailed_service(request, service_id):

    service = get_object_or_404(Services, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/detailed_service.html', context)






