from django.contrib import admin
from django.urls import include, path

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('order/', include('orders.urls')),
    path('menu/', include('menu.urls')),
    path('cart/', include('cart.urls')),
    path('api/', include('api.urls')),
]
