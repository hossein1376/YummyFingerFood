from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class OrderModel(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='شماره سفارش')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='کاربر')
    order_date = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ثبت سفارش')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='آخرین ویرایش')
    editable = models.BooleanField(default=True, verbose_name='قابل ویرایش')

    description = models.TextField(
        blank=True, null=True, max_length=500, verbose_name='توضیحات')

    class Meta:
        verbose_name = ('سفارش')
        verbose_name_plural = ('سفارش ها')
