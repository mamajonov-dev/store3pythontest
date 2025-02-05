from django.contrib import admin
from .models import *

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(ProductModel)
class ProdAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Userprofile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username']

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'owner']

@admin.register(BasketModel)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['product', 'owner', 'count', 'ordered','basket_price']
