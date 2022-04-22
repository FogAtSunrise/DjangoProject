from django import forms
from .models import Product, Category

categories = Category.objects.all().values_list('name')
# creating a form
class ProductForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Product

        # specify fields to be used
        fields = [
            "name",
            "description",
            "price",
            "size",
            "category",
            "image"
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'item-name', 'type': 'text'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'about-textarea', 'rows': '3'}),
            'size': forms.TextInput(attrs={'class': 'form-control', 'id': 'item-size', 'type': 'text'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'category': forms.Select(choices=categories, attrs={'class': 'form-select', 'id': 'category-select'}),
            #'image': forms.ImageField(attrs={'id': 'choose-foto'})

        }

