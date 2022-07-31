from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    readonly_fields = ('created_jalali', 'updated_jalali')
    list_display = ['id', 'created_jalali',
                    'updated_jalali', 'editable', 'paid', ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    def created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d - %H:%M')

    def updated_jalali(self, obj):
        return datetime2jalali(obj.updated).strftime('%Y/%m/%d - %H:%M')

    created_jalali.short_description = 'تاریخ ثبت سفارش'
    updated_jalali.short_description = 'آخرین ویرایش'


admin.site.register(Order, OrderAdmin)
