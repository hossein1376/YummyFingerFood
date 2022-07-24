from django.urls import path

from .views import ProfilePageView, SignupPageView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
]