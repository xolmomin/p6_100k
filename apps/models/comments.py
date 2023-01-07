from django.db.models import Model, ForeignKey, PROTECT, CharField, TextField


class Comment(Model):
    author = ForeignKey('auth.User', PROTECT)
    name = CharField(max_length=255)
    content = TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name