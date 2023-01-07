from django.db.models import Model, CharField


class Region(Model):
    name = CharField(max_length=100)


class District(Model):
    name = CharField(max_length=100)
    region_id = CharField(max_length=100)
