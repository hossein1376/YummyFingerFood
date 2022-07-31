from django.forms import ModelForm

from .models import Order


class OrderCreationForm(ModelForm):
    class Meta:
        model = Order
        fields = ('description',)
