from django.conf.urls import url
from .views import Events, EventDetails

urlpatterns = [
    url(r'^', Events),
    url(r'(?P<slug>[-\w]+)/$', EventDetails),

]
