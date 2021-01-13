from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LandlordProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address = models.CharField(max_length=20, null=False, blank=False)
    house_name = models.CharField(max_length=20, null=True, blank=True)
    post_code = models.CharField(max_length=9, null=False, blank=False)

    def __str__(self):
        return self.user.username



