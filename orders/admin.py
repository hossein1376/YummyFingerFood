from django.contrib import admin

from .models import OrderModel


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_date', 'updated_at')


admin.site.register(OrderModel, OrderAdmin)
