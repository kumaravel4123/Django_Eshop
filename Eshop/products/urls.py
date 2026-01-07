from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.productView, name= 'product_page')
]