from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    price = models.PositiveIntegerField(verbose_name='قیمت (هزار تومن)')
    description = models.CharField(
        max_length=300, blank=True, null=True, verbose_name='توضیحات (در صورت نیاز)')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Cake(Menu):
    class Meta:
        verbose_name = ('کیک')
        verbose_name_plural = ('کیک ها')


class Salad(Menu):
    class Meta:
        verbose_name = ('سالاد')
        verbose_name_plural = ('سالاد ها')
