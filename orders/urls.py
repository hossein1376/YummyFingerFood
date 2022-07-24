from django.urls import path

from .views import (NewOrderView, OrderDeleteView, OrderDetailView,
                    OrderEditView, OrderHistoryView)

urlpatterns = [
    path('new/', NewOrderView.as_view(), name='new_order'),
    path('history/', OrderHistoryView.as_view(), name='order_history'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('<int:pk>/edit', OrderEditView.as_view(), name='order_edit'),
    path('<int:pk>/delete', OrderDeleteView.as_view(), name='order_delete'),
]
