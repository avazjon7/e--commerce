from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'products'
    ordering = ['-id']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product-detail.html'
    context_object_name = 'product'

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/add-product.html'
    fields = ['name', 'description', 'price', 'category', 'discount', 'quantity']
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product-list.html'
    success_url = reverse_lazy('product_list')

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/edit-product.html'
    fields = ['name', 'description', 'price', 'category', 'discount', 'quantity']
    success_url = reverse_lazy('product_list')

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=product_id)


