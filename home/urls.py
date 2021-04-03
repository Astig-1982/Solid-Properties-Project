from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('personalised/', views.personalised_shopping, name='personalised'),
    path('personalised_shopping_about/', views.personalised_shopping_about, name='personalised_shopping_about'),
]
