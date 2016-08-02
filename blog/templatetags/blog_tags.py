from django import template
from ..models import BlogPost
register = template.Library()


@register.inclusion_tag('blog/tags/based.html')
def posts(number=5, template='blog/tags/posts.html'):
    return {'template': template,
            'posts': BlogPost.objects.all()[:number]}