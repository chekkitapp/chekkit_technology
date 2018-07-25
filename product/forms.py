from django.forms import ModelForm, Form

from ussdapp.models import ProductLine, Product

class ProductLineForm(ModelForm):
	class Meta:
		model= ProductLine
		fields=['product_name', 'description',]

class ProductForm(ModelForm):
	class Meta:
		model = Product
		exclude = ['product_code']
