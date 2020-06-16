# resale/urls.py
from django.urls import path
from . import views

app_name = 'resale'

urlpatterns = [
    path('<slug:slug>/', views.category, name='category'),
]









