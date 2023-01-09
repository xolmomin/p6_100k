from django.db.models import Model, ForeignKey, PROTECT, CharField, TextField, CASCADE, IntegerChoices


class Comment(Model):
    class Rate(IntegerChoices):
        Ajoyib = 1, 'Ajoyib'
        Yaxshi = 2, 'Yaxshi'
        Qoniqarli = 3, 'Qoniqarli'
        Yomon = 4, 'Yomon'
        Judayomon = 5, 'Judayomon'

    author = ForeignKey('apps.User', PROTECT)
    name = CharField(max_length=255)
    content = TextField()
    product = ForeignKey('apps.Product', CASCADE)
    rate = CharField(max_length=25, choices=Rate.choices, default=Rate.Qoniqarli)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
