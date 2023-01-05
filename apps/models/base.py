from django.contrib.auth.models import User
from django.db.models import Model, DateTimeField, SlugField, ForeignKey, PROTECT, TextField, CharField, CASCADE, \
    BooleanField
from django.db.models import Model, DateTimeField, SlugField, ForeignKey, PROTECT, TextField, CASCADE
from django.db.models import CharField
from django_resized import ResizedImageField

from apps.models import Store


class Product(Model):
    title = CharField(max_length=255)
    main_picture = ResizedImageField(size=[500, 300], upload_to='%m')
    price = CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)
    slug = SlugField(max_length=255, unique=True)
    store = ForeignKey(Store, CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Comment(Model):
    author = ForeignKey(User, PROTECT)
    name = CharField(max_length=255)
    content = TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name


class Stream(Model):
    name = CharField(max_length=255)
    donation = CharField(max_length=20)                     # hayriya uchun mablag`
    reduce = CharField(max_length=20)                       # narxini kamaytirish uchun mablag`
    user = ForeignKey('User', CASCADE)                      # oqim yaratgan foydalanuchi
    product = ForeignKey('apps.base.Product', CASCADE)      # oqim uchun mahsulot
    is_area = BooleanField(default=False)                   # hududsiz qabul qilish