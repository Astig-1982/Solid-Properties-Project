from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='cart'),
    path('add_to_cart/<service_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<service_id>', views.remove_from_cart, name='remove_from_cart'),
    path('remove_address/<service_id>', views.remove_address, name='remove_address'),
]