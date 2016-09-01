from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.job_list, name='job_list'),
    url(r'^(?P<slug>[-\w]+)/$', views.job_description, name='job_description'),
    url(r'^(?P<slug>[-\w]+)/$', views.upload_file, name='job_description'),
    #url(r'^(?P<slug>[-\w]+)/$', views.upload_file.as_view(), name='job_description'),
]