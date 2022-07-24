from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from orders.models import OrderModel

from .forms import OrderForm


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
    ordering = ['-order_date']
    paginate_by = 5


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

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


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
