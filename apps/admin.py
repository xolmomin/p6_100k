from django.contrib.admin import ModelAdmin, register

from apps.models import Store, Product, Category


@register(Store)
class StoreAdmin(ModelAdmin):
    list_display = ('id', 'name')


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'store_name')
    exclude = ('slug',)

    def store_name(self, obj: Product):  # noqa
        return obj.store.name


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'title')
