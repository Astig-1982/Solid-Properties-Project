from django import forms
from .models import Properties


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ('landlord', 'street_address', 'house_name',
                  'post_code', 'no_of_bedrooms')


