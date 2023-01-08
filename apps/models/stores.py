from django.db.models import Model, CharField
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
