from django.contrib import admin
from .models import Order, OrderLineItem

"""Register models to the admin console"""

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)