from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('menu/', include('menu.urls')),
    path('api/', include('api.urls')),
]
