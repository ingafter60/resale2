# resale/views
from django.shortcuts import render, get_object_or_404
from . models import Category

# Create your views here.
def home(request):
	categories = Category.objects.all()	
	context = {'section': 'home', 'categories': categories}
	return render(request, 'Resale/index.html', context)


def category_list(request, slug=None):
	cat_list = get_object_or_404(Category, slug=slug)	
	context = {'catlist':cat_list}
	return render(request, 'Resale/categories.html', context)




