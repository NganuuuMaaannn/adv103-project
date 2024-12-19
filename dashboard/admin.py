from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header= 'Inventory Management System'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)