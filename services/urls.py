from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('detailed_service/<service_id>', views.detailed_service, name='detailed_service'),
]