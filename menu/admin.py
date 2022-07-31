from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_jalali', 'updated_jalali',]
    readonly_fields = ('created_jalali', 'updated_jalali')
    ordering = ('-created',)

    def created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d - %H:%M')
    
    def updated_jalali(self, obj):
        return datetime2jalali(obj.updated).strftime('%Y/%m/%d - %H:%M')
    
    created_jalali.short_description = 'اضافه شده در'
    updated_jalali.short_description = 'آخرین ویرایش در'


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['category', 'name', 'price',
                    'available', 'description', 'created_jalali', 'updated_jalali']
    list_filter = ['category', 'available', 'created', 'updated']
    list_editable = ['name', 'price', 'available', 'description']
    readonly_fields = ('created_jalali', 'updated_jalali')

    def created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d - %H:%M')

    def updated_jalali(self, obj):
        return datetime2jalali(obj.updated).strftime('%Y/%m/%d - %H:%M')

    created_jalali.short_description = 'اضافه شده در'
    updated_jalali.short_description = 'آخرین ویرایش در'
