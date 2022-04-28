from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display =['name']
     list_per_page = 2
     search_fields = ['name']
     list_filter = ['name']

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
     list_display =['name','description','cost']
     list_per_page = 5
     search_fields = ['name','cost','description']
     list_filter =['name','cost','description']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
     search_fields = ('name',)
     list_display = ('name','adress',)
admin.site.register([Order,OrderItem])