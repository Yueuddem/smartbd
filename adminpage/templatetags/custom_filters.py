from django import template

register = template.Library()

@register.filter
def getattr_custom(obj, attr_name):
    """객체에서 필드 값을 가져오는 커스텀 템플릿 필터"""
    return getattr(obj, attr_name, '')