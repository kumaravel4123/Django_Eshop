from django.shortcuts import render, redirect
from django.urls import reverse

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
    else:
        context = {
            'query' : query,
            'products' : None
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

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk' : self.object.pk})


    # Overriding the queryset to pre-fetch and the product images along side products

    def get_queryset(self):
        return Product.objects.prefetch_related('images')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            image = form.save(commit = False)
            image.product = self.object
            image.save()
            return redirect(self.get_success_url())


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    fields = '__all__'
    success_url = '/'

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = '/'


# Edit Product Image

from .models import ProductImage

class EditProductImage(UpdateView):
    model = ProductImage
    template_name = 'products/image_edit.html'
    fields = '__all__'
    context_object_name = 'image'

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk' : self.object.product.pk})
    
class DeleteProductImage(DeleteView):
    model = ProductImage
    template_name = 'products/image_del.html'
    context_object_name = 'image'

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk' : self.object.product.pk})

