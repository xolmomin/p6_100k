from django.db.models import Model, CharField, IntegerField, DateTimeField, SlugField, ForeignKey, CASCADE, \
    BooleanField, TextField, ImageField, TextChoices, FileField, SET_NULL, DecimalField
from django.utils.text import slugify

from apps.models.base import BaseModel


class Product(Model):
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    price = DecimalField(max_digits=9, decimal_places=2)
    bonus = IntegerField()
    reserve = IntegerField()
    video = FileField(upload_to='products/', null=True, blank=True)
    free_delivery = BooleanField(default=False)
    store = ForeignKey('apps.Store', CASCADE)
    category = ForeignKey('apps.Category', CASCADE)
    slug = SlugField(max_length=255, unique=True)
    created_at = DateTimeField(auto_now_add=True)

    @property
    def stream_count(self):
        return self.stream_set.count()

    @property
    def image_url(self):
        try:
            url = self.productimage_set.first().image.url
        except (ValueError, AttributeError):
            url = 'https://via.placeholder.com/400x400'
        return url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Product.objects.filter(slug=self.slug).exists():
                slug = Product.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
        super().save(*args, **kwargs)


class ProductImage(Model):
    product = ForeignKey('apps.Product', CASCADE)
    image = ImageField(upload_to='image/', default='media/product-default.jpg')


class Order(BaseModel):
    class Status(TextChoices):
        NEW = 'new', 'Yangi'
        ACCEPTED = 'accepted', 'Qabul qilindi'
        SHIPPING = 'shipping', 'Yetkazilmoqda'
        DELIVERED = 'delivered' 'Yetkazib berildi'
        CALLBACK = 'callback', "Qayta qo'ng'iroq"
        SPAM = 'spam', 'Spam'
        HOLD = 'hold', 'Hold'
        ARXIV = 'arxiv', 'Arxivlandi'

    name = CharField(max_length=255)
    phone = CharField(max_length=25)
    status = CharField(max_length=50, choices=Status.choices, default=Status.NEW)
    address = CharField(max_length=255, null=True, blank=True)
    region = ForeignKey('apps.Region', SET_NULL, null=True, blank=True)
    product = ForeignKey('apps.Product', SET_NULL, null=True)
    operator = ForeignKey('apps.User', SET_NULL, null=True)
    stream = ForeignKey('apps.Stream', SET_NULL, null=True)

    class Meta:
        ordering = ('-created_at',)
