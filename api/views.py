from rest_framework import generics
from menu.models import Cake, Salad
from .serializers import CakeSerializer, SaladSerializer


class CakeAPIView(generics.ListAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer


class SaladAPIView(generics.ListAPIView):
    queryset = Salad.objects.all()
    serializer_class = SaladSerializer
