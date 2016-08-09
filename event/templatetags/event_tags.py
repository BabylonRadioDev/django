from django import template
from ..models import Event
register = template.Library()


@register.inclusion_tag('event/tags/based.html')
def events(number=5, template='event/tags/events.html'):
    return {'template': template,
            'events': Event.objects.all()[:number]}