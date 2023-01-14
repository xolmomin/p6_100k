from django.core.exceptions import ValidationError
from django.forms import ModelForm, IntegerField

from apps.models import Stream


class CreateStreamForm(ModelForm):
    donation = IntegerField(required=False)
    reduce = IntegerField(required=False)
    class Meta:
        model = Stream
        fields = ('name', 'product', 'donation', 'reduce')

    def clean_reduce(self):
        if not self.data.get('reduce', False):
            return 0
        elif not (1000 < self.data['reduce'] < 50000):
            raise ValidationError('Reduce must be in 100 and 5000!')

        return self.data['reduce']

    def clean_donation(self):
        if not self.data.get('donation', False):
            return 0
        elif not (100 < self.data['donation'] < 5000):
            raise ValidationError('Donation must be in 100 and 5000!')
        return self.data['donation']


class UpdateStreamForm(ModelForm):
    class Meta:
        model = Stream
        fields = ('is_area',)