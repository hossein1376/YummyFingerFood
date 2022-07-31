from django.contrib.auth import get_user_model
from django.db import models
from menu.models import Product


User = get_user_model()


class Order(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='شماره سفارش')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='کاربر')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ثبت سفارش')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='آخرین ویرایش')
    editable = models.BooleanField(default=True, verbose_name='قابل ویرایش')
    paid = models.BooleanField(default=False, verbose_name='پرداخت شده')
    description = models.TextField(
        blank=True, null=True, max_length=500, verbose_name='توضیحات')

    class Meta:
        verbose_name = ('سفارش')
        verbose_name_plural = ('سفارش ها')
        ordering = ('-created',)
        
    def __str__(self):
        return f'سفارش به شماره: {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='سفارش')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='محصول')
    price = models.PositiveIntegerField(verbose_name='قیمت (هزار تومن)')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    
    class Meta:
        verbose_name = ('قلم کالا')
        verbose_name_plural = ('اقلام کالا')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity