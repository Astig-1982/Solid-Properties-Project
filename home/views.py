from django.shortcuts import render
from services.models import Category

# Create your views here.


def index(request):

    all_categories = Category.objects.all()
    categories = all_categories.order_by('name')

    context = {
        'categories': categories
    }

    return render(request, "home/index.html", context)


def about(request):
    """
    This view displays the about page
    """
    context = {}

    return render(request, 'home/about.html', context)


def personalised_shopping(request):
    """
    This view displays the personalised shoppoing page
    """
    context = {
        'personalised': True,
    }

    return render(request, 'home/personalised.html', context)


def personalised_shopping_about(request):
    """
    This view displays the personalised shopping page accessed from about page
    """
    context = {
        'personalised': True,
        'from_about': True,
    }

    return render(request, 'home/personalised.html', context)
