from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models.base import Store, Product


# Register your models here.

@admin.register(Store)
class StoreAdmin(ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'store_name')

    def store_name(self, obj: Product):
        return obj.store.name
