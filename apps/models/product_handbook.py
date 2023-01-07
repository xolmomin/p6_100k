from django.db.models import Model, CharField, IntegerField, DateTimeField, SlugField, ForeignKey, CASCADE
from django_resized import ResizedImageField


class Product(Model):
    title = CharField(max_length=255)
    main_picture = ResizedImageField(size=[500, 300], upload_to='%m')
    price = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    slug = SlugField(max_length=255, unique=True)
    store = ForeignKey('apps.Store', CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
