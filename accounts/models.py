from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    address = models.TextField(max_length=100, verbose_name='آدرس')
    zip_code = models.CharField(max_length=10, verbose_name='کد پستی')

    def __str__(self):
        return self.username
