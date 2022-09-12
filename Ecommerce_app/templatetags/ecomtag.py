from django import template
from django.shortcuts import get_object_or_404


from Ecommerce_app.models import Footer,Header
from product_app.models import Category

register = template.Library()


@register.simple_tag
def ecom_cat():
    return Category.objects.all()


@register.simple_tag
def ecom_foot():
    return get_object_or_404(Footer)


@register.simple_tag
def ecom_header():
    return get_object_or_404(Header)
