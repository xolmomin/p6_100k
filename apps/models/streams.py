from django.db.models import BooleanField, Model, ForeignKey, CharField, CASCADE, PositiveIntegerField, IntegerField
from django_resized import ResizedImageField

from apps.models.base import BaseModel


class Stream(BaseModel):
    name = CharField(max_length=255)
    donation = PositiveIntegerField(default=0)  # hayriya uchun mablag`
    reduce = PositiveIntegerField(default=0)  # narxini kamaytirish uchun mablag`
    user = ForeignKey('apps.User', CASCADE)  # oqim yaratgan foydalanuchi
    product = ForeignKey('apps.Product', CASCADE)  # oqim uchun mahsulot
    views = IntegerField(default=0)  # ko`rilgan oqimlar soni
    is_area = BooleanField(default=False)  # hududsiz qabul qilish


class Store(BaseModel):
    image = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to='shops')
    name = CharField(max_length=255)
    short_des = CharField(max_length=255)

    def __str__(self):
        return self.name


class Region(Model):
    name = CharField(max_length=100, default='Tashkent')


class District(Model):
    name = CharField(max_length=100, default='Tashkent')
    region = ForeignKey(Region, CASCADE)
