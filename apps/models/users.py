from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DecimalField, PositiveIntegerField
from django_resized import ResizedImageField

from apps.models.payments import PaymentHistory


class User(AbstractUser):
    phone = CharField(max_length=255, unique=True)
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users')
    balance = DecimalField(max_digits=30, decimal_places=2, default=0)  # main balance
    bonus = PositiveIntegerField(default=0)  # bonus balance
    deposit = DecimalField(max_digits=30, decimal_places=2, default=0)  # deposit balance

    @property
    def payout(self):
        amount = PaymentHistory.objects.filter(user_id=self.id, status=PaymentHistory.StatusChoices.ACCEPTED)
        return sum(amount.values_list('amount', flat=True))
