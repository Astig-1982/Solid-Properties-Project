from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    icon = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Services(models.Model):

    class Meta:
        verbose_name_plural = 'Services'
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, related_name='categories')
    name = models.CharField(max_length=254)
    price_variation = models.BooleanField(default=False, null=True, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name




