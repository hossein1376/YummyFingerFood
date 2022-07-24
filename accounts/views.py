from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfilePageView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'registration/profile.html'
    login_url = 'login'
    success_url = reverse_lazy('profile')

    fields = ('username', 'first_name', 'last_name',
              'email', 'address', 'zip_code',)

    def get_object(self):
        return self.request.user
