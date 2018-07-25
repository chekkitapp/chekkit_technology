from django.shortcuts import render
from django.http import HttpResponse
from ussdapp.models import ProductLine
# Create your views here.

def overview(request):
	# productlines = ProductLine.objects.all()
	# context = {
	# 'productlines': productlines
	# }
	# return render(request, 'frontend/overview.html', context)
	return HttpResponse("Some dummy text for testing")