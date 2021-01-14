from django.db import models

# Create your models here.


class Main_Category(models.Model):

    class Meta:
        verbose_name_plural = 'Main Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Services(models.Model):

    class Meta:
        verbose_name_plural = 'Services'
    main_category = models.ForeignKey('Main_Category', null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, related_name='categories')
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    bedrooms_dependent = models.BooleanField(default=False, null=True, blank=True)
    one_time_fee_display = models.BooleanField(default=False, null=True, blank=True)
    price_variation = models.BooleanField(default=False, null=True, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name




