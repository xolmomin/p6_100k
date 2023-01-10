from django.contrib.admin import ModelAdmin, register

from apps.models import Store, Product, Category, Contact
from apps.models.payments import PaymentHistory


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
    exclude = ('slug',)
    list_display = ('id', 'title')


@register(PaymentHistory)
class PaymentAdmin(ModelAdmin):
    list_display = ('user', 'amount', 'status')


@register(Contact)
class ContactAdmin(ModelAdmin):
    pass
