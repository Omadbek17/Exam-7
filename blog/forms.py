from django import forms
from .models import Customer, Product


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class ProductListModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()
