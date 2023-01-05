from django.forms import ModelForm

from apps.models import Comment, User


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ()


class EditProfile(ModelForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'phone')
