from django.shortcuts import render
from . forms import ProductLineForm, ProductForm
# from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from product.models import ProductLine
from django.views.generic.detail import DetailView
# Create your views here.
def add_productlines(request):
	if request.method == 'POST':
		form = ProductLineForm(request.POST, request.FILES)
		if form.is_valid:
			# new_form= form.cleaned_data
			form.save()

			return HttpResponseRedirect('/')
	else:
		form = ProductLineForm()
	return render(request, 'product/add_productline.html', {'form': form} )

class ProductLineView(DetailView):
	model = ProductLine
	template_name = 'product/product_detail.html'
	content_object_name = 'productline'

def generate_product_codes(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid:
			# new_form= form.cleaned_data
			form.save()

			return HttpResponseRedirect('/')
	else:
		form = ProductForm()
	return render(request, 'product/generate_product_codes.html', {'form': form} )	