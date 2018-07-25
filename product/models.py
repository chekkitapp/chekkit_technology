from django.db import models
from django.urls import reverse


# Create your models here.
from django.db import models
from account.models import Manufacturer, Location

class ProductLine(models.Model):
	product_name = models.CharField(max_length = 100)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(upload_to = 'images', blank=True)
	manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True)
	quantity = models.IntegerField(default = 0, blank = True, null = True)
	production_date = models.DateTimeField(auto_now_add = True)
	created_on = models.DateTimeField(auto_now_add = True)
	date_modified = models.DateTimeField(auto_now = True)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.product_name

	class Meta :
		ordering = ['-created_on']



class Batch(models.Model):
	production_date = models.DateTimeField()
	expiry_date = models.DateTimeField()
	batch_number = models.IntegerField(unique=True, blank=True, null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	origin = models.CharField(max_length = 50)
	created_on = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	is_active = models.BooleanField(default = False)
	manufacturer = models.ForeignKey('Manufacturer', on_delete = models.CASCADE)

	def __str__(self):
		return "{}: {}".format(self.location.manufacturer_name, self.batch_number)

	class Meta :
		ordering = ['-created_on']



