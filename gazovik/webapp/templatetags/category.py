from django import template

from ..models import Tovar

register = template.Library()


@register.inclusion_tag('webapp/tags/tovar_list.html', takes_context=True)
def category_list(context, cat_id, num):
    """
    Товары по категориям
    """

    result = Tovar.objects.filter(category_id=cat_id).order_by('-id')[:num]

    return {
        'category': result
    }


@register.inclusion_tag('webapp/tags/tovar_list_slick.html', takes_context=True)
def category_slick(context, cat_id, num):
    """
    Товары по категориям в виде слайдера
    """

    result = Tovar.objects.filter(category_id=cat_id).order_by('-id')[:num]

    return {
        'category': result
    }



# @register.inclusion_tag('webapp/tags/tovar_list.html', takes_context=True)
# def category_list(context, cat_id, num):
#     """
#     Товары по категориям
#     """
#
#     print ('cat_id:', cat_id)
#
#     result = Tovar.objects.filter(category_id=cat_id).order_by('-id')[:num]
#
#     # .select_related('author__profile__user').order_by('-created_at')[:num]
#
#     return {
#         'category': result
#     }
