import re
from django import template
from men.models import *

register = template.Library()

@register.simple_tag(name='get_cats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('men/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'category_selected': category_selected}