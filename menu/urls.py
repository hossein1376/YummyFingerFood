from django.urls import path
from .views import (
    CakeView, SaladView
)

urlpatterns = [
    path('cakes/', CakeView.as_view(), name='cake'),
    path('salad/', SaladView.as_view(), name='salad'),
]