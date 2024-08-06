from django.contrib import admin
from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


# Register your models here.


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_ver', 'version_number', 'version_name', 'is_version_active')
    list_filter = ('product_ver', 'is_version_active',)
    search_fields = ('product_ver', 'version_name',)
