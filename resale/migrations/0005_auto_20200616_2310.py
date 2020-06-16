# Generated by Django 3.0.7 on 2020-06-16 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0004_auto_20200616_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_condition',
            new_name='condition',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pro_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='productimages',
            old_name='proimg_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='productimages',
            old_name='product_productimages',
            new_name='images',
        ),
    ]
