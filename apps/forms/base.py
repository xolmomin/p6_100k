from django.forms import ModelForm

from apps.models.base import Comment


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ()