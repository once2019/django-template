from django.contrib import admin
from .models import Product,Post,Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Category)