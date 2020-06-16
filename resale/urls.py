# resale/urls.py
from django.urls import path
from . import views

app_name = 'resale'

urlpatterns = [
    # path('<slug:slug>/', views.detail, name='detail'),
    path('<slug:slug>/', views.category_list, name='category_list'),
]