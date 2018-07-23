from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	code = models.IntegerField(unique=True)
	name = models.CharField(max_length = 200)
	industry = models.CharField(max_length= 400)

	def __str__(self):
		return self.name


# class Users(models.Model):
	# class Employees():

	# class Real():

class Location(models.Model):
	name = models.CharField(max_length = 300)
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	@property
	def manufacturer_name(self):
		return self.manufacturer.name
	