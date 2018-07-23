from django.db import models

# Create your models here.
from django.db import models
from account.models import Manufacturer, Location

class ProductLine(models.Model):
	product_name = models.CharField(max_length = 200)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(upload_to = 'images', blank=True)
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.product_name


class Batch(models.Model):
	production_date = models.DateTimeField()
	expiry_date = models.DateTimeField()
	batch_number = models.IntegerField(unique=True, blank=True, null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)

	def __str__(self):
		return "{}: {}".format(self.location.manufacturer_name, self.batch_number)


class Product(models.Model):
	product_code=models.IntegerField(unique=True)
	product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=False)
	batch_number = models.ForeignKey(Batch, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.product_code)