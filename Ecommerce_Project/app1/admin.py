from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryReg(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Product)
class ProductReg(admin.ModelAdmin):
    list_display = ('p_name', 'p_price')
    prepopulated_fields = {"slug": ('p_name',)}


# Register your models here.
