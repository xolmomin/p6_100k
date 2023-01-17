from django.db.models import Model, CharField, IntegerField, DateTimeField, SlugField, ForeignKey, CASCADE, \
    BooleanField, TextField, ImageField, TextChoices, FileField
from django.utils.text import slugify


class Product(Model):
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    price = IntegerField()
    bonus = IntegerField()
    reserve = IntegerField()
    video = FileField(upload_to='product/', null=True, blank=True)
    free_delivery = BooleanField(default=False)
    store = ForeignKey('apps.Store', CASCADE)
    category = ForeignKey('apps.Category', CASCADE)
    slug = SlugField(max_length=255, unique=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

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


class ProductOrders(Model):
    class OrderStatus(TextChoices):
        YANGI = 'Yangi'
        QABUL = 'Qabul qilindi'
        YETKAZILMOQDA = 'Yetkazilmoqda'
        YETKAZILDI = 'Yetkazib berildi'
        QAYTA = 'Qayta qo\'ng\'iroq'
        SPAM = 'Spam'
        HOLD = 'Hold'
        ARXIV = 'Arxivlandi'

    name = CharField(max_length=255)
    region = CharField(max_length=255)
    phone = CharField(max_length=25)
    status = CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.YANGI)
    product = ForeignKey('apps.Product', CASCADE)
    created_at = DateTimeField(auto_now_add=True)
