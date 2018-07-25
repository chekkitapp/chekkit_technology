from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ussdapp.models import Manufacturer, Location

# Register your models here.
class ManufacturerAdmin(admin.ModelAdmin):
	pass

class LocationAdmin(admin.ModelAdmin):
	pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)