#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from forms import ContactForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Event, Ticket
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from datetime import date, time, datetime


class EventListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def Events(request):
    eventlist = Event.objects.filter(visibility=1)
    return render(request, 'event_list.html', {'eventList': eventlist, })


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

# def EventDetails(request, id_Event):
#     c = {}
#     event = get_object_or_404(Event, pk=id_Event)
#     #ticketHere = get_object_or_404(ticket, pk = id_Event)
#     listTik = Ticket.objects.filter(event_id=id_Event)
#     return render(request, 'event_detail.html/'.format(id_Event), {'listTik': listTik, 'event': event}, c)

# def EventDay(request, year, month, day):
#     y = int(year)
#     m = int(month)
#     d = int(day)
#     dateDay = datetime(y, m, d)
#     model = Event
#     #for eve in Event:
#       #  dateTest = eve.date_start|date:'Y/m/d'
#        # if (dateTest == dateDay):
#         #    listEventDay += get_object_or_404(Event, date_start = eve.date_start)
#         #endif
#     #endfor
#     #eventDay = Event.objects.filter(date_start = dateDay)
#     eventDay = Event.objects.filter(visibility=1)
#     return render(request, 'event_day.html', {'listEventDay': listEventDay, })

