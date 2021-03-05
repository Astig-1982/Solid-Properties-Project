from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_property, name='add_property'),
    path('remove_property/<property_id>', views.remove_property, name='remove_property'),
    path('activate/<property_id>', views.activate_deactivate, name='activate_deactivate'),
]
