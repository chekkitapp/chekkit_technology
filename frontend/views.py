from django.shortcuts import render
from product.models import ProductLine
# Create your views here.

def overview(request):
	productlines = ProductLine.objects.all()
	context = {
	'productlines': productlines
	}
	return render(request, 'frontend/overview.html', context)