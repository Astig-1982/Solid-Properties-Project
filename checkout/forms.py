from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('landlord_profile', 'full_name', 'email', 'phone_number',
                  'country', 'postcode', 'town_or_city',
                  'street_address1', 'street_address2',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated labels
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False
            if self.fields[field].required:
                placeholder = f'{field}*'
            else:
                placeholder = field
            placeholder = placeholder.replace('_',  ' ')
            if field != 'country':
                self.fields[field].widget.attrs['placeholder'] = \
                                                placeholder.capitalize()
