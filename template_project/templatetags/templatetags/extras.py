from django import template

register = template.Library()

@register.filter
def inc(curr, val):
    print(type(curr), type(val))
    return float(curr)+float(val)

# division a b

@register.simple_tag
def division(a, b, to_int=False):
    return int(float(a)//float(b)) if to_int else float(a)/float(b)
