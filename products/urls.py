from django.urls import path
from .views import ClearProductsView, ProductListCreate, index

urlpatterns = [
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/clear/', ClearProductsView.as_view(), name='clear_products'),
    path('', index, name='index'),
]