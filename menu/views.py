from django.views.generic import ListView

from .models import Cake, Salad


class Menu(ListView):
    model = ''
    template_name = 'menu.html'
    context_object_name = 'items'


class CakeView(Menu):
    model = Cake
    extra_context = {'category_name': 'کیک ها'}


class SaladView(Menu):
    model = Salad
    # extra_context = {'category_name': 'سالاد ها'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = 'سالاد ها'
        context['category_name'] = category_name
        return context
