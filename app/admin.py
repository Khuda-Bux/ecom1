from django.contrib import admin
from .models import(
    Product,
    Cart,
)
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price',
    'discounted_price', 'description',  
    'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product', 'quantity']


    
