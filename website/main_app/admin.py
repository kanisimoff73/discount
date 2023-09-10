from django.contrib import admin
from .models import *


class ShopsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name", "slug")
    search_fields = ("name", "slug")


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name", "slug")
    search_fields = ("name", "slug")


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "photo", "price", "link", "cat", "shop")
    list_display_links = ("id", "name", "photo", "price", "link", "cat", "shop")


admin.site.register(Shops, ShopsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
