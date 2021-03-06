from django.contrib import admin
from .models import Order, OrderLineItem, OrderLineItemAnonym

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderLineItemAdminInlineAnonym(admin.TabularInline):
    model = OrderLineItemAnonym
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline, OrderLineItemAdminInlineAnonym)

    readonly_fields = ('order_number', 'date',
                       'grand_total')

    fields = ('order_number', 'landlord_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'grand_total')

    list_display = ('order_number', 'date',
                    'full_name', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
