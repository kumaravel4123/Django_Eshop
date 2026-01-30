from django import forms
from .models import ProductImage,Product


BOOTSTRAP_ATTRS = {
    'class' : 'form-control'
}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'title', 'desc', 'price', 'stock', 'thumbnail']
        widgets = {
            'title' : forms.TextInput(attrs=BOOTSTRAP_ATTRS),
            'desc' : forms.Textarea(attrs=BOOTSTRAP_ATTRS),
            'price' : forms.NumberInput(attrs=BOOTSTRAP_ATTRS),
            'stock' : forms.NumberInput(attrs=BOOTSTRAP_ATTRS),
            'thumbnail' : forms.ClearableFileInput(attrs=BOOTSTRAP_ATTRS)
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['img','caption']