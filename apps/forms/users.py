from django.forms import ModelForm, IntegerField

from apps.models import Comment, User, Region
from apps.models.users import Favorite


class ProfileModelForm(ModelForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'phone', 'address', 'region', 'district')

    def clean_region(self):
        region = Region.objects.get(id=self.cleaned_data.get('region'))
        return region.name


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'product', 'name')


class FavoriteModelForm(ModelForm):
    id = IntegerField()

    class Meta:
        model = Favorite
        exclude = ()


# class LoginForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('phone', 'password')
#
#     def clean_phone(self):
#         phone: str = self.data.get('phone')
#         if phone.startswith('+'):
#             return phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
#         return phone
