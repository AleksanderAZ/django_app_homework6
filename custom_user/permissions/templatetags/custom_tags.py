from django import template

register = template.Library()

@register.simple_tag
def infousers(users):
    return users.count()



