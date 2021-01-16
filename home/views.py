from django.shortcuts import render
from services.models import Category

# Create your views here.


def index(request):

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, "home/index.html", context)
