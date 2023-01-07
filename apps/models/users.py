from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DecimalField
from django_resized import ResizedImageField


class User(AbstractUser):
    phone = CharField(max_length=255, unique=True)
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users')
    balance = DecimalField(max_digits=30, decimal_places=2)  # main balance
    bonus = DecimalField(max_digits=30, decimal_places=2)  # bonus balance
    deposit = DecimalField(max_digits=30, decimal_places=2)  # deposit balance
