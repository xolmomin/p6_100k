from uuid import uuid4

from django.db.models import DecimalField, ForeignKey, CharField, TextChoices, CASCADE

from apps.models.base import BaseModel


class PaymentHistory(BaseModel):
    class StatusChoices(TextChoices):
        PENDING = 'pending', 'Kutilmoqda'
        ACCEPTED = 'accepted', "To'lab berildi"
        CANCELED = 'canceled', 'Bekor qilingan'

    user = ForeignKey('apps.User', CASCADE)
    amount = DecimalField(max_digits=12, decimal_places=2)
    card_number = CharField(max_length=16)
    status = CharField(choices=StatusChoices.choices, default=StatusChoices.PENDING, max_length=10)
    transaction_id = CharField(max_length=255, default=uuid4)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payment history'
        ordering = ('-created_at',)
