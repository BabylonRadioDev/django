#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from forms import ContactForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Event, Ticket
from django.utils import timezone


class EventListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def Events(request):
    eventlist = Event.objects.filter(visibility=1)
    return render(request, 'event_list.html', {'eventList': eventlist, })


# def EventDetails(request, id_Event):
#     c = {}
#     event = get_object_or_404(Event, pk=id_Event)
#     #ticketHere = get_object_or_404(ticket, pk = id_Event)
#     listTik = Ticket.objects.filter(event_id=id_Event)
#
#     return render(request, 'event_detail.html/'.format(id_Event), {'listTik': listTik, 'event': event}, c)


class EventDetail(DetailView):
    template_name = 'event_detail.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['listTik'] = Ticket.objects.all()
        # context['event'] = Event.objects.all()
        return context

    def get_success_url(self):
        return reverse('event-detail')
