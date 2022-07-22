from rest_framework import serializers

from menu.models import Cake
from menu.models import Salad


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ('id', 'title', 'price', 'description',)


class SaladSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salad
        fields = ('id', 'title', 'price', 'description',)