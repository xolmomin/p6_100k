from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, IntegerField

from apps.models import Comment, User
from apps.models.users import Favorite


class ProfileModelForm(ModelForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'phone', 'address', 'region', 'district')


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'product', 'name')


class FavoriteModelForm(ModelForm):
    id = IntegerField()

    class Meta:
        model = Favorite
        exclude = ()
