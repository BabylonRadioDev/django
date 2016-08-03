# from django.conf.urls import url
# from .views import Events, EventDetails
#
# urlpatterns = [
#     url(r'^', Events),
#     url(r'(?P<slug>[-\w]+)/$', EventDetails),
#
# ]
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import *
from django.contrib import admin


from .views import Events, EventDetail
admin.autodiscover()



urlpatterns = [
    url(r'^$', Events, name='event-list'),
    url(r'^(?P<slug>[-\w]+)/$', EventDetail.as_view(), name='event-detail'),
]