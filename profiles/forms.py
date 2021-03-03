from django import forms
from .models import LandlordProfile


class BillingForm(forms.ModelForm):
    class Meta:
        model = LandlordProfile
        fields = ('default_full_name', 'default_email',
                  'default_phone_number', 'default_country',
                  'default_postcode', 'default_town_or_city',
                  'default_street_address1', 'default_street_address2',)
