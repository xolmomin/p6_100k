from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DecimalField, PositiveIntegerField, Model, EmailField, ForeignKey, CASCADE
from django_resized import ResizedImageField

from apps.models.payments import PaymentHistory


class User(AbstractUser):
    phone = CharField(max_length=255, unique=True)
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users')
    address = CharField(max_length=555, blank=True, null=True)
    balance = DecimalField(max_digits=30, decimal_places=2, default=0)  # main balance
    bonus = PositiveIntegerField(default=0)  # bonus balance
    deposit = DecimalField(max_digits=30, decimal_places=2, default=0)  # deposit balance
    coin = PositiveIntegerField(default=0)

    @property
    def payout(self):
        amounts = self.paymenthistory_set.filter(
            status=PaymentHistory.StatusChoices.ACCEPTED
        ).values_list('amount', flat=True)
        return sum(amounts)


class Contact(Model):
    phone = CharField(max_length=255)
    email = EmailField(max_length=255)
    telegram = CharField(max_length=255)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'


class Favorite(Model):
    user = ForeignKey('apps.User', CASCADE)
    product = ForeignKey('apps.Product', CASCADE)
