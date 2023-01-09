from django.forms import ModelForm

from apps.models.users import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'phone', 'address')
