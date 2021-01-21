from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_property, name='add_property'),
]