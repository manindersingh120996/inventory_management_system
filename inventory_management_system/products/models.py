from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class category (BaseModel):
    category_name= models.CharField(max_length=100)
    slug=models.SlugField(unique=True, null=True, blank= True)

    def save(self, *args,**kwargs):
        self.slug =slugify (self.category_name)
        super(category, self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name
    

class product (BaseModel):
    product_name= models.CharField(max_length=100)
    category = models.ForeignKey(category, related_name="products", on_delete=models.CASCADE)
    price=models.FloatField()
    product_description =models.TextField()
    slug=models.SlugField(unique=True, null=True, blank= True)
    product_image = models.ImageField(upload_to='product')

    def save(self, *args,**kwargs):
        self.slug =slugify (self.product_name)
        super(product, self).save(*args,**kwargs)

    def __str__(self):
        return self.product_name