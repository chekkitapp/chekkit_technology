from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ussdapp.models import Product, ProductLine, Batch


class ProductLineAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'manufacturer','description', 'photo')
	list_filter = ['is_active', 'manufacturer']
	search_fields = ['product_name',]

class ProductAdmin(admin.ModelAdmin):
	pass

class BatchAdmin(admin.ModelAdmin):
	pass

admin.site.register(Batch, BatchAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductLineAdmin)