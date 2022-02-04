from django.urls import path,include
from .views import (
    ProductCreateView,
    CategoryCreateView,
    ProductListView,
    CategoryListView,
)


urlpatterns = [
    path("create-product/",ProductCreateView.as_view()),
    path("product-list/", ProductListView.as_view(), name="product-list"),
    path("create-category/",ProductCreateView.as_view()),
    path("category-list/", ProductListView.as_view(), name="category-list"),
]