from django.forms import ModelForm

from apps.models import ProductOrders


class OrderForm(ModelForm):
    class Meta:
        model = ProductOrders
        exclude = ()
