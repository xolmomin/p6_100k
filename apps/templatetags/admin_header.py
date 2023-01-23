from django.template import Library

register = Library()


@register.filter(name='is_active')
def check_active_url(url, path):
    return url.split('/')[-1] == path