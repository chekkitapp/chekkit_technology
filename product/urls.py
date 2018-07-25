from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.add_productlines, name = 'add_productlines'),
    path('<int:pk>/', views.ProductLineView.as_view(), name = 'detail_productline'),
    path('generate/', views.generate_product_codes, name = 'generate_product_codes'),
    
]
