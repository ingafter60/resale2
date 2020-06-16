# resale/views
from django.shortcuts import render, get_object_or_404
from . models import Category

# Create your views here.
def home(request):
	categories = Category.objects.all()	
	context = {'section': 'home', 'categories': categories}
	return render(request, 'Resale/index.html', context)

# def category(request):
# 	categories = Category.objects.all()	
# 	context = {'section': 'home', 'categories': categories}
# 	return render(request, 'Resale/categories.html' )


def category(request, slug=None):
	# posts = get_object_or_404(Category, slug=slug)	
	categories =  Category.objects.all()	
	context = {'categories':categories}
	return render(request, 'Resale/categories.html', context)




