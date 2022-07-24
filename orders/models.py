from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

from menu.models import Cake, Salad

User = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='کاربر')
    order_date = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت سفارش')

    cake = models.ManyToManyField(
        Cake, blank=True, verbose_name='کیک ها')
    salad = models.ManyToManyField(
        Salad, blank=True, verbose_name='سالاد ها')
    description = models.TextField(
        blank=True, null=True, max_length=500, verbose_name='توضیحات')

    class Meta:
        verbose_name = ('سفارش')
        verbose_name_plural = ('سفارش ها')

    def __str__(self):
        return f'سفارش کاربر {self.user} | شماره سفارش: {self.id}'
    
    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})