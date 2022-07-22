from django.urls import path
from .views import CakeAPIView, SaladAPIView

urlpatterns = [
    path('cake/', CakeAPIView.as_view()),
    path('salad/', SaladAPIView.as_view()),
]
