from django.urls import path

from .views import productView, searchProducts

urlpatterns = [
    # path('all/', productView, name = 'products'),
    path('products/', productView, name= 'product_page'),
    path('serach/', searchProducts, name= 'search_products')
]