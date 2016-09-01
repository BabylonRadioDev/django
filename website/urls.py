"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
import home.views


urlpatterns = [
    url(r'^$', home.views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^events/', include('event.urls', namespace='event')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^join/', include('join.urls', namespace='join')),
    url(r'^sirtrevor/', include('sirtrevor.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r"^payments/", include("pinax.stripe.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)