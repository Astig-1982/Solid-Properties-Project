from django import forms
from .models import Properties


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ('landlord', 'street_address', 'house_name',
                  'post_code', 'no_of_bedrooms')

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
            self.fields[field].widget.attrs['placeholder'] = \
                placeholder.capitalize()

