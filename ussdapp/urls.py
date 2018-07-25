from django.urls import path
from . import views

# app_name = 'ussdapp'

urlpatterns = [
    path('getcodes', views.getcodes, name = 'ussdapp'),
    path('checkcode', views.checkcode, name = 'ussdapp'),

]