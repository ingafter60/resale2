# resale/urls.py
from django.urls import path
from . import views

app_name = 'resale'

urlpatterns = [
	path('', views.home, name='home')	
]