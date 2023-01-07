from django.db.models import Model, CharField, IntegerField, DateTimeField, SlugField, ForeignKey, CASCADE, BooleanField
from django.utils.text import slugify
from django_resized import ResizedImageField


class Product(Model):
    title = CharField(max_length=255)
    main_picture = ResizedImageField(size=[500, 300], upload_to='%m')
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
