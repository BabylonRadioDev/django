#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from forms import ContactForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from event.models import Event
from event.models import ticket, UserProfile
from django.utils import timezone

class EventListView(ListView):
    model = Event
    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def Events(request):
    eventList = Event.objects.filter(visibility = 1)
    return render(request, 'eventslist.html', {'eventList' : eventList, })

def EventDetails(request, id_Event):
    #model = Event
    event = get_object_or_404(Event, pk = id_Event)
    #ticketHere = get_object_or_404(ticket, pk = id_Event)
    listTik = ticket.objects.filter(event_id = id_Event)
            
    return render(request, 'events.html/'.format(id_Event), {'listTik' : listTik, 'event' : event})

def contact(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST, instance=event)

        if form.is_valid(): # check if the data are good
            
            # here we can make some stuff to work on the data
            title = form.cleaned_data['title']
            location = form.cleaned_data['location']
            link = form.cleaned_data['link']
            date_start = form.cleaned_data['date_start']
            date_end = form.cleaned_data['date_end']
            description = form.cleaned_data['description']
            mail = form.cleaned_data['mail']
            slug = form.cleaned_data['slug']
            visibility = form.cleaned_data['visibility']
            paying = form.cleaned_data['paying']
            
            form.save(commit=False)
            envoi = True

    else:
        form = ContactForm() 

    return render(request, 'event/form.html', locals())