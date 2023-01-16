from django.contrib.admin import ModelAdmin, register, StackedInline
from django.urls import reverse
from django.utils.html import format_html

from apps.models import Store, Product, Category, Contact, PaymentHistory, ProductImage, Stream


@register(Store)
class StoreAdmin(ModelAdmin):
    list_display = ('id', 'name')


class ImageAdmin(StackedInline):
    model = ProductImage


@register(Product)
class ProductAdmin(ModelAdmin):
    inlines = [ImageAdmin]
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


@register(Stream)
class StreamAdmin(ModelAdmin):
    list_display = ('name', 'donation', 'reduce', 'user', 'product_name', 'is_area')

    def product_name(self, obj):
        a = f'''<a style="font-weight:bold;text-decoration:none;" href="{reverse('admin:apps_product_change', args=(obj.product.pk,))}">{obj.product.title}</a>'''
        return format_html(a)