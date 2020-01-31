from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    """ get the OrderLineItem instances and prepare for showing inline in Order model in admin """
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    """ add OrderLineItems prepared in the above function to the relevant order """
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
