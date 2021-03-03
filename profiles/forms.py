from django import forms
from .models import LandlordProfile


class BillingForm(forms.ModelForm):
    class Meta:
        model = LandlordProfile
        fields = ('default_full_name', 'default_email',
                  'default_phone_number', 'default_country',
                  'default_postcode', 'default_town_or_city',
                  'default_street_address1', 'default_street_address2',)

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
            placeholder = placeholder.replace('default', ' ')
            if field != 'country':
                self.fields[field].widget.attrs['placeholder'] = \
                                                placeholder
