from django.db.models import BooleanField, Model, ForeignKey, CharField, CASCADE


class Stream(Model):
    name = CharField(max_length=255)
    donation = CharField(max_length=20)  # hayriya uchun mablag`
    reduce = CharField(max_length=20)  # narxini kamaytirish uchun mablag`
    user = ForeignKey('apps.User', CASCADE)  # oqim yaratgan foydalanuchi
    product = ForeignKey('apps.Product', CASCADE)  # oqim uchun mahsulot
    is_area = BooleanField(default=False)  # hududsiz qabul qilish
