from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField, BooleanField, Model, TextChoices, PROTECT, ForeignKey, TextField
from django_resized import ResizedImageField

from apps.utils.token import bot_activation_token


class User(AbstractUser):
    phone = CharField(max_length=255, unique=True)
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users')
    telegram_id = CharField(max_length=55, null=True, blank=True)
    bot_is_activate = BooleanField(default=False)
    bot_active_token = CharField(max_length=255, unique=True)


class Tickets(Model):
    class SenderTextChoice(TextChoices):
        XARIDOR = 'customer', 'xaridor'
        KURYER = 'kuryer', 'kuryer'
        ADMIN = 'admin', 'admin'
        SOTUVCHI = 'salesman', 'sotuvchi'
        BOSHQA = 'other', 'boshqa'

    class PurposeTextChoice(TextChoices):
        MUAMMO = 'issue', 'muammo'
        TAKLIF = 'suggestion', 'taklif'

    author = ForeignKey(User, PROTECT)
    sender = CharField(max_length=55, choices=SenderTextChoice.choices)
    sender_name = CharField(max_length=255)
    phone_number = CharField(max_length=20)
    ticket_purpose = CharField(max_length=55, choices=PurposeTextChoice.choices)
    message = TextField()
