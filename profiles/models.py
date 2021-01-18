from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class LandlordProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address = models.CharField(max_length=20, null=False, blank=False)
    house_name = models.CharField(max_length=20, null=True, blank=True)
    post_code = models.CharField(max_length=9, null=False, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):

    if created:
        LandlordProfile.objects.create(user=instance)





