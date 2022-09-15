from django.contrib import admin
from .models import product
from .models import category
# Register your models here.

admin.site.register(product)
admin.site.register(category)