import uuid
from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from profiles.models import LandlordProfile
from services.models import Services
from properties.models import Properties

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    landlord_profile = models.ForeignKey(LandlordProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)  
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs. This function
        will be executed if the user is logged in.
        """
        self.grand_total = self.lineitems.aggregate(Sum(
                           'lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def update_total_for_anonym(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs. This function
        will be executed if the user is not logged in.
        """
        self.grand_total = self.lineitemsanonym.aggregate(Sum(
                          'lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# this model is for each line item if the user is logged in
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(Services, null=False, blank=False, on_delete=models.CASCADE)
    the_property = models.ForeignKey(Properties, null=False, blank=False, on_delete=models.CASCADE, related_name='properties') # the property the service is purchased for
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False) # total cost of the service for the property

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """

        if self.service.price_variation:
            self.lineitem_total = self.service.price * \
                                  self.the_property.no_of_bedrooms
        else:
            self.lineitem_total = self.service.price

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Service {self.service.name} \
            on order {self.order.order_number}'


# this model is for each line item if the user is not logged in
class OrderLineItemAnonym(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitemsanonym')
    service = models.ForeignKey(Services, null=False, blank=False, on_delete=models.CASCADE)
    no_of_bedrooms = models.DecimalField(max_digits=1, decimal_places=0, null=False, blank=False, editable=False) # the number of bedrooms for which the service is purchased
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False) # total cost of the service for the number of bedrooms is purchased

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = int(self.service.price) * \
            int(self.no_of_bedrooms)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Service {self.service.name} \
            on order {self.order.order_number}'
