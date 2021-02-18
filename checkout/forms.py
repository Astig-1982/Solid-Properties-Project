from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'country', 'post_code', 'town_or_city',
                  'street_address_1', 'street_address_2',)
