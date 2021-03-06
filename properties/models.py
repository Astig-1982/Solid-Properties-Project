from django.db import models
from profiles.models import LandlordProfile

# Create your models here.


class Properties(models.Model):

    class Meta:
        verbose_name_plural = 'Properties'

    landlord = models.ForeignKey(LandlordProfile, null=True, on_delete=models.SET_NULL, related_name='properties')
    street_address = models.CharField(max_length=80, null=False, blank=False)
    house_name = models.CharField(max_length=20, null=True, blank=True)
    post_code = models.CharField(max_length=9, null=False, blank=False)
    no_of_bedrooms = models.DecimalField(max_digits=1, decimal_places=0)
    activate = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.street_address
