from django.template import Library
from apps.models import District

register = Library()


@register.filter(name='get_district')
def get_district(regions, region):
    a = []
    for i in District.objects.filter(region_id=region):
        a.append(i.name)
    return a
