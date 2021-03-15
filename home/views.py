from django.shortcuts import render
from services.models import Category

# Create your views here.


def index(request):

    categories = Category.objects.all()

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
