from django.forms import ModelForm
from apps.models.payments import PaymentHistory


class PaymentForm(ModelForm):
    class Meta:
        model = PaymentHistory
        fields = ('amount', 'card_number')
