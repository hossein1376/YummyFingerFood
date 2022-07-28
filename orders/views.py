from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import OrderForm
from .models import OrderModel


class NewOrderView(LoginRequiredMixin, CreateView):
    form_class = OrderForm
    template_name = 'orders/order_new.html'
    login_url = 'login'

    success_url = reverse_lazy('order_history')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = OrderModel
    template_name = 'orders/order_history.html'
    login_url = 'login'

    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            user=self.request.user).order_by('-order_date')
        return queryset


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = OrderModel
    template_name = 'orders/order_detail.html'
    login_url = 'login'

    context_object_name = 'order'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


class OrderEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrderModel
    template_name = 'orders/order_edit.html'
    login_url = 'login'

    fields = ('cake', 'salad', 'description')
    context_object_name = 'order'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = OrderModel
    template_name = 'orders/order_delete.html'
    login_url = 'login'

    context_object_name = 'order'
    success_url = reverse_lazy('order_history')

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False
