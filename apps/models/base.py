from django.contrib.auth.models import User
from django.db.models import Model, DateTimeField, SlugField, ForeignKey, PROTECT, TextField
from django.db.models import CharField
from django_resized import ResizedImageField


class Product(Model):
    title = CharField(max_length=255)
    main_picture = ResizedImageField(size=[500, 300], upload_to='%m')
    price = CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)
    slug = SlugField(max_length=255, unique=True)

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
