# #-*- coding: utf-8 -*-
# from django.http import HttpResponse
# from django.shortcuts import render
# from datetime import datetime
# from forms import ContactForm
# from django.shortcuts import get_object_or_404
# from django.views.generic import ListView
# # from event.models import ticket, UserProfile
# from django.utils import timezone
#
#
from django.core.urlresolvers import reverse
# from .forms import BlogForm
from .models import Event#, ticket#, UserProfile
# from .models import BlogPost, CategoryToPost
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.views.generic import (DetailView,
                                  ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)


#
#
# class EventListView(ListView):
#     model = Event
#     def get_context_data(self, **kwargs):
#         context = super(EventListView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context
#
class EventList(ListView):
    model = Event
    template_name = 'event_list.html'
    # ordering = ["-timestamp"]

    def get_success_url(self):
        return reverse('event-list')

class EventDetail(DetailView):
    model = Event
    template_name = 'event_detail.html'

    def get_success_url(self):
        return reverse('event-detail')

# def Events(request):
#     eventList = Event.objects.filter(visibility = 1)
#     return render(request, 'eventslist.html', {'eventList' : eventList, })
#
# def EventDetails(request, id_Event):
#     #model = Event
#     event = get_object_or_404(Event, pk = id_Event)
#     #ticketHere = get_object_or_404(ticket, pk = id_Event)
#     listTik = ticket.objects.filter(event_id = id_Event)
#
#     return render(request, 'events.html/'.format(id_Event), {'listTik' : listTik, 'event' : event})
#
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST, instance=event)
#
#         if form.is_valid(): # check if the data are good
#
#             # here we can make some stuff to work on the data
#             title = form.cleaned_data['title']
#             location = form.cleaned_data['location']
#             link = form.cleaned_data['link']
#             date_start = form.cleaned_data['date_start']
#             date_end = form.cleaned_data['date_end']
#             description = form.cleaned_data['description']
#             mail = form.cleaned_data['mail']
#             slug = form.cleaned_data['slug']
#             visibility = form.cleaned_data['visibility']
#             paying = form.cleaned_data['paying']
#
#             form.save(commit=False)
#             envoi = True
#
#     else:
#         form = ContactForm()
#
#     return render(request, 'event/form.html', locals())



# class CreateBlogPost(CreateView):
#     model = BlogPost
#     template_name = 'blogpost_create.html'
#     form_class = BlogForm
#
#     def get_success_url(self):
#         return reverse('blog-list')
#
#     def get_context_data(self, **kwargs):
#         context = super(CreateBlogPost, self).get_context_data(**kwargs)
#         context['action'] = reverse('blog-create')
#         return context
#
#     def form_valid(self, form):
#         candidate = form.save(commit=False)
#         candidate.user = User.objects.get(username=self.request.user)  # use your own profile here
#         candidate.save()
#         return HttpResponseRedirect(self.get_success_url())
#
# class BlogUpdate(UpdateView):
#     model = BlogPost
#     form_class = BlogForm
#     template_name = 'blogpost_create.html'
#
#     def get_success_url(self):
#         return reverse('blog-list')
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogUpdate, self).get_context_data(**kwargs)
#         context['action'] = reverse('blog-update', kwargs={'slug': self.get_object().slug})
#         return context
#
# class BlogDelete(DeleteView):
#     model = BlogPost
#     form_class = BlogForm
#     template_name = 'blogpost_delete.html'
#
#     def get_success_url(self):
#         return reverse('blog-list')
#
