from django.views.generic import ListView

from .models import Category, Product

from cart.forms import CartAddProductForm


class MenuView(ListView):
    model = Product
    template_name = 'menu.html'
    queryset = Product.objects.filter(available=True).order_by('category', 'created')
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_names = Category.objects.all().order_by('created')
        context['category_names'] = category_names
        
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        
        return context
