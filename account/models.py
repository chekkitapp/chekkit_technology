from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	name = models.CharField(max_length = 100)
	code = models.IntegerField(default = 0, blank = True, null = True, unique = True)
	industry = models.CharField(max_length = 100)
	modified = models.DateTimeField(auto_now = True)
	is_active = models.BooleanField(default = False)
	created_on = models.DateTimeField(auto_now_add = True)
	contact = models.ForeignKey('Contact', on_delete = models.CASCADE)

	def __unicode__(self) :
		return u'{} Code:{} industry:{}'.format(self.name, str(self.code), self.industry)

	def __str__(self):
		return self.name

	class Meta :
		ordering = ['-created_on']


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
	