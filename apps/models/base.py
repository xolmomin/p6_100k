from django.db.models import BooleanField, Model, DateTimeField, SlugField, ForeignKey, PROTECT, TextField, CharField, \
    CASCADE, IntegerField
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


# TODO Javlon Commentni alohida file ga olib ciqib qoying
class Comment(Model):
    author = ForeignKey('auth.User', PROTECT)
    name = CharField(max_length=255)
    content = TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name


class Stream(Model):
    name = CharField(max_length=255)
    donation = CharField(max_length=20)  # hayriya uchun mablag`
    reduce = CharField(max_length=20)  # narxini kamaytirish uchun mablag`
    user = ForeignKey('auth.User', CASCADE)  # oqim yaratgan foydalanuchi
    product = ForeignKey('apps.Product', CASCADE)  # oqim uchun mahsulot
    is_area = BooleanField(default=False)  # hududsiz qabul qilish
