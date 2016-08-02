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


from .views import EventList, EventDetail

admin.autodiscover()



urlpatterns = [
    url(r'^$', EventList.as_view(), name='event-list'),
    # url(r'^create/$', CreateBlogPost.as_view(), name='blog-create'),
    # url(r'^edit/(?P<slug>[-\w]+)/$', BlogUpdate.as_view(), name='blog-update'),
    # url(r'^delete/(?P<slug>[-\w]+)/$', BlogDelete.as_view(), name='blog-delete'),
    # url(r'^category/$', CategoryList.as_view(), name='category-list'),
    # url(r'^category/(?P<category>[-\w]+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^(?P<slug>[-\w]+)/$', EventDetail.as_view(), name='event-detail'),
]