from typing import List
from attr import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from app1.models import Product , Category

# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("product-list")
    template_name = 'app1/product.html'
    
class CategoryCreateView(CreateView):
    model = Category
    fields = "__all__"
    template_name = 'app1/category.html'
    success_url = reverse_lazy("category-list")
class ProductListView(ListView):
    model = Product
    template_name = 'app1/product_list.html'
    queryset = Product.objects.all().order_by("created_at")

class CategoryListView(ListView):
    model = Category
    template_name = 'app1/category_list.html'
    queryset = Category.objects.all()
    
    
