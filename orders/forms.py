from django.forms import ModelForm

from .models import OrderModel


class OrderForm (ModelForm):
    class Meta:
        model = OrderModel
        fields = ('description',)
