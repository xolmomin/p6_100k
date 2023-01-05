from django.contrib.admin import ModelAdmin, register

from apps.models import Store, Product


@register(Store)
class StoreAdmin(ModelAdmin):
    list_display = ('id', 'name')


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'store_name')

    def store_name(self, obj: Product):
        return obj.store.name
