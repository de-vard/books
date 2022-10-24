from django import template
from books.models import *

register = template.Library()
# Большое желание было сделать теги ))) их не использую


@register.simple_tag()
def sort_plus():
    sort_name = Book.objects.order_by('price')
    return sort_name

@register.simple_tag()
def sort_minus():
    sort_name = Book.objects.order_by('-price')
    return sort_name
