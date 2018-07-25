from django import forms
from . models import ProductLine, Product

class ProductLineForm(forms.ModelForm):
	class Meta:
		model= ProductLine
		fields=['photo','product_name', 'description']
		widgets = {
            'product_name': forms.TextInput(attrs={'cols': 20, 'rows': 20, 'class': 'form-control','placeholder':'name'}),
            'description': forms.TextInput(attrs={'cols': 20, 'rows': 20, 'class': 'form-control', 'placeholder':'description'}),
        	'photo': forms.FileInput(attrs={'required': False})
        }

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude = ['product_code']
