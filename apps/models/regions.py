from django.db.models import Model, CharField, ForeignKey, CASCADE


class Region(Model):
    name = CharField(max_length=100)


class District(Model):
    name = CharField(max_length=100)
    region = ForeignKey(Region, on_delete=CASCADE)
