from django.urls import path

from .views import order_create

urlpatterns = [
    path('new/', order_create, name='order_new'),
]
