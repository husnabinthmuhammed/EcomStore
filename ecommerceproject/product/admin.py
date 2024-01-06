from django.contrib import admin

# Register your models here.
from .models import Category, Cart, Product

admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Product)