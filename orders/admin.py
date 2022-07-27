from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from .models import OrderModel


class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    readonly_fields = ('order_date', 'updated_at')
    list_display = ['id', 'order_date_jalali',
                    'updated_at_jalali', 'editable', ]

    def order_date_jalali(self, obj):
        return datetime2jalali(obj.order_date).strftime('%Y/%m/%d - %H:%M')

    def updated_at_jalali(self, obj):
        return datetime2jalali(obj.updated_at).strftime('%Y/%m/%d - %H:%M')

    order_date_jalali.short_description = 'تاریخ ثبت سفارش'
    updated_at_jalali.short_description = 'آخرین ویرایش'


admin.site.register(OrderModel, OrderAdmin)
