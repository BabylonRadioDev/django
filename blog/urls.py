from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import *  # NOQA
from django.contrib import admin


from .views import (BlogList,
                    BlogDetail,
                    CategoryDetail,
                    CategoryList)

admin.autodiscover()



urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog-list'),
    # url(r'^create/$', CreateBlogPost.as_view(), name='blog-create'),
    # url(r'^edit/(?P<slug>[-\w]+)/$', BlogUpdate.as_view(), name='blog-update'),
    # url(r'^delete/(?P<slug>[-\w]+)/$', BlogDelete.as_view(), name='blog-delete'),
    url(r'^category/$', CategoryList.as_view(), name='category-list'),
    url(r'^category/(?P<category>[-\w]+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^(?P<slug>[-\w]+)/$', BlogDetail.as_view(), name='blog-detail'),
]