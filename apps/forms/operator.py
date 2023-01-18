from django.forms import CharField, Form

from apps.models import Order


class OrderEditStatus(Form):
    id = CharField(max_length=20)
    status = CharField(max_length=30)

    def save(self):
        _id = self.cleaned_data.get('id')
        status = self.cleaned_data.get('status')
        Order.objects.filter(id=_id).update(status=status)
        return
