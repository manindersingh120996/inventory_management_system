# Generated by Django 3.2.15 on 2022-09-16 18:45

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.filepath),
        ),
    ]