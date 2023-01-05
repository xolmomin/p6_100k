from django.contrib.auth.models import User
from django.db.models import Model, DateTimeField, SlugField, ForeignKey, PROTECT, TextField, CASCADE
from django.db.models import CharField
from django_resized import ResizedImageField


class Store(Model):
    image = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to='shops')
    name = CharField(max_length=255)
    short_des = CharField(max_length=255)

    class Meta:
        verbose_name = "Stores"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name


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
