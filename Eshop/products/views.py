from django.shortcuts import render

from .models import Product

# Create your views here.

def productView(request):
    template = 'products/products.html'
    context = {
        'current_page' : 'products',
        'products' : Product.objects.all()
    }

    return render(request, template_name= template, context= context)

# search Products
from django.db.models import Q

def searchProducts(request):
    template = 'products/search_results.html'
    query =  request.GET.get('q')
    if query:
        search_results = Product.objects.filter(
            Q(title__icontains = query) |
            Q(desc__icontains = query)
        )

        context = {
            'query' : query,
            'products' : search_results
        }

    return render(request, template_name=template, context= context)

# CRUD Operations using Generic Class Based Views of Django

from django.views.generic import ( CreateView, DetailView,
                                   UpdateView, DeleteView )

# ListView has already been implemented using a function above : productView()

class CreateProduct(CreateView):
    model = Product
    template_name = 'products/add_product.html'
    fields = '__all__'
    # redirection url for successful creation of resource
    success_url = '/'

class AddProductImage(CreateView):
    model = Product
    template_name = 'product/add_images.html'
    fields = "__all__"

    success_url = '/'

from django.views.generic.edit import FormMixin
# This mixin provides ability to render forms from the `form class`
from .forms import ProductImageForm

class ProductDetail(FormMixin,DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'
    # Providing form class for product image
    form_class = ProductImageForm

    # Overriding the queryset to pre-fetch and the product images along side products

    def get_queryset(self):
        return Product.objects.prefetch_related('images')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abcd'] = 'yuhoo'

        return context
    


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    fields = '__all__'
    success_url = '/'

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = '/'

