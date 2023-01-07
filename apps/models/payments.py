from uuid import uuid4

from django.db.models import Model, DecimalField, ForeignKey, CharField, TextChoices, CASCADE, DateTimeField


class PaymentHistory(Model):
    class StatusChoices(TextChoices):
        PENDING = 'pending'
        ACCEPTED = 'accepted'
        CANCELED = 'canceled'

    user = ForeignKey('apps.User', CASCADE)
    amount = DecimalField(max_digits=12, decimal_places=2)
    card_number = CharField(max_length=16)
    status = CharField(choices=StatusChoices.choices, default=StatusChoices.PENDING)
    transaction_id = CharField(max_length=255, default=uuid4)
    created_at = DateTimeField(auto_now_add=True)
