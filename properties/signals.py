from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Properties


@receiver(post_save, sender=Properties)
def activate_dezactivate(sender, instance, created, **kwargs):

    instance.properties.activate_dezactivate()











