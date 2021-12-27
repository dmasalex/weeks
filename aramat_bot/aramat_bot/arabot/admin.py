from django.contrib import admin

from .models import Product, Procedure, TypeProcedure, TypeProduct, Customer


@admin.register(Customer, )
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'tg_first_name', 'tg_last_name', 'tg_username', 'comment', 'phone', 'display_product', 'display_procedure')
    search_fields = ['tg_username']
    list_filter = ('tg_id', 'tg_username')


@admin.register(Procedure, )
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment', 'price', 'image', 'display_typeprocedure')
    search_fields = ['title', 'display_typeprocedure']
    list_filter = ('title', 'typeprocedure', 'price')


@admin.register(Product, )
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment', 'price', 'image', 'display_typeproduct')
    search_fields = ['title', 'display_typeproduct']
    list_filter = ('title', 'typeproduct', 'price')


@admin.register(TypeProduct, )
class TypeProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment')
    search_fields = ['title']


@admin.register(TypeProcedure, )
class TypeProcedureAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment')
    search_fields = ['title']
