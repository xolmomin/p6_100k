from django.db.models import Model, CharField, IntegerField, DateTimeField, SlugField, ForeignKey, CASCADE, \
    BooleanField, TextField, SET_NULL
from django.utils.text import slugify
from django_resized import ResizedImageField


class Product(Model):
    title = CharField(max_length=255)
    main_picture = ResizedImageField(size=[500, 300], upload_to='%m')
    description = TextField(null=True, blank=True)
    price = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    slug = SlugField(max_length=255, unique=True)
    bonus = IntegerField()
    free_delivery = BooleanField(default=False)
    reserve = IntegerField()
    store = ForeignKey('apps.Store', CASCADE)
    category = ForeignKey('apps.Category', CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @property
    def stream_count(self):
        return self.stream_set.count()

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


class ProductOrders(Model):  # main pagedigi productslada buyurtmalar uchun model
    product = ForeignKey('apps.Product', CASCADE)  # productga ulangan boladu
    region = ForeignKey('apps.Region', SET_NULL, null=True, blank=True)
    user = ForeignKey('apps.User', CASCADE)  # km zakaz qilingani
    phone = IntegerField()

