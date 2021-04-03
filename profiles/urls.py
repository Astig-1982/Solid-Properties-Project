from django.urls import path
from . import views

urlpatterns = [
    path('', views.landlord_profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('billing_details/', views.billing_details, name='billing_details'),
    path('personalised_shopping_profile/', views.personalised_shopping_profile, name='personalised_shopping_profile'),
]