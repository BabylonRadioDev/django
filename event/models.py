from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from autoslug import AutoSlugField
from sirtrevor.fields import SirTrevorField


# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#
#     def __str__(self):
#         return self.user.get_username()
#
#
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, created = UserProfile.objects.get_or_create(user=instance)
#
#
# post_save.connect(create_user_profile, sender=User)


class Event(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')
    location = models.CharField(max_length=150)
    link = models.CharField(max_length=150, null=True)
    main_image = models.ImageField(upload_to=None, height_field=None, width_field=None,
                                   null=True)  # find a general size
    date_start = models.DateTimeField(auto_now=False, verbose_name="Event Start", null=True)
    date_end = models.DateTimeField(auto_now=False, verbose_name="Event End", null=True)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Event Creation", null=True)
    date_update = models.DateTimeField(auto_now=True, verbose_name="Event Update", null=True)
    description = SirTrevorField()
    author = models.ForeignKey(User)

    mail = models.EmailField(max_length=100, null=True)
    visibility = models.BooleanField()
    paying = models.BooleanField()

    def __unicode__(self):
        return self.title


# class ticket(models.Model):
#     name = models.CharField(max_length=50, null=True)
#     price = models.DecimalField(max_digits=200, null=True, decimal_places=2)  # if 0 -> free
#     quantity = models.IntegerField(null=True)
#     sold = models.IntegerField(null=True)
#     event_id = models.ForeignKey(Event)
#
#     def __unicode__(self):
#         return self.name
