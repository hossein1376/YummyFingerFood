from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='اسم (به صورت جمع)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='اضافه شده در')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش در')
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE, verbose_name='دسته بندی')
    name = models.CharField(max_length=200, db_index=True, verbose_name='اسم')
    description = models.CharField(max_length=200, blank=True, verbose_name='توضیحات (در صورت نیاز)')
    price = models.PositiveIntegerField(verbose_name='قیمت (هزار تومن)')
    available = models.BooleanField(default=True, verbose_name='موجود')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='اضافه شده در')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='آخرین ویرایش در')

    class Meta:
        ordering = ('name',)
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name
