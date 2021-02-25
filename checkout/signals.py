from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem, OrderLineItemAnonym


@receiver(post_save, sender=OrderLineItem)
def update_order(sender, instance, created, **kwargs):

    instance.order.update_total()


@receiver(post_save, sender=OrderLineItemAnonym)
def update_order_anonym(sender, instance, created, **kwargs):

    instance.order.update_total_for_anonym()


@receiver(post_delete, sender=OrderLineItem)
def update_delete_order(sender, instance, **kwargs):

    instance.order.update_total()
    instance.order.update_total_for_anonym()
