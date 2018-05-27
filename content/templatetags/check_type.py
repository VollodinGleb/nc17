from django import template
register = template.Library()


@register.filter(name='obj_type')
def check_type(obj):
    try:
        return obj.__class__.__name__
    except:
        return "None"


@register.filter(name='field_type')
def field_type(field, ftype):
    return check_type(field.field.widget, ftype)
