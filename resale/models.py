# resale/models.py
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# CATEGORY MODEL/TALBE
class Category(models.Model):
	
	cat_name = models.CharField(max_length=50)
	cat_description = models.CharField(max_length=255)
	image = models.ImageField(upload_to='category/', blank=True, null=True)
	slug 	 = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug and self.cat_name:
			self.slug = slugify(self.cat_name)
		super(Category, self).save(*args, **kwargs)	

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.cat_name	

	def get_absolute_url(self):
		return reverse('resale:category', args=[str(self.slug)])



# PRODUCT MODEL/TALBE
class Product(models.Model):

	CONDITION_TYPE = (
		("New", "New"),
		("Used", "Used")
	)

	name 		= models.CharField(max_length=100)
	owner 		= models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=500)
	condition 	= models.CharField(max_length=100, choices=CONDITION_TYPE)
	category_product= models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	brand 		= models.ForeignKey('Brand' , on_delete=models.SET_NULL, null=True)
	price 		= models.DecimalField(max_digits=10, decimal_places=2)
	image 		= models.ImageField(upload_to='main_product/', blank=True, null=True)
	created 	= models.DateTimeField(default=timezone.now)
	slug 		= models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug and self.name:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)	

	def __str__(self):
		return self.name



# BRAND MODEL/TALBE
class Brand(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name	


# PRODUCTIMAGES MODEL/TALBE
class ProductImages(models.Model):
    images	= models.ForeignKey(Product , on_delete=models.CASCADE)
    image			= models.ImageField(upload_to='products/', blank=True , null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'        

    def __str__(self):
        return self.images.name







'''
PRODUCT
=======

1NF: Product
------------
name, description, condition, price, published

2NF: Product
------------
name, description, condition(new, used), price, published

3NF: Product
------------
name, owner, description, condition(new, used), price, published

4NF: Product
------------
name, owner, description, condition(new, used), price, published(add time saving)


CATEGORY
========

1NF: Category
------------
name, image




'''
