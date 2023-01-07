from uuid import uuid4

from django.db.models import Model, DecimalField, ForeignKey, CharField, TextChoices


class PaymentHistory(Model):
    class StatusChoices(TextChoices):
        PENDING = 'pending'
        ACCEPTED = 'accepted'
        CANCELED = 'canceled'

    user = ForeignKey('apps.User')
    amount = DecimalField(max_digits=12, decimal_places=2)
    card_number = CharField(max_length=16)
    status = CharField(choices=StatusChoices.choices, default=StatusChoices.PENDING)
    transaction_id = CharField(max_length=255, default=uuid4())
