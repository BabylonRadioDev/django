from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# from tinymce.widgets import TinyMCE
from sirtrevor.fields import SirTrevorField

# Create your models here.

### Manages the state of the post
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

### Manages the nameing convention of the uploaded files
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


### Category of the post
class Category(models.Model):
    cat_title = models.CharField(max_length=50, null=True, blank=True, default='')
    slug = AutoSlugField(populate_from='cat_title')

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.cat_title

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.id})


### The structure of the blog post
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    intro = models.TextField()
    body = SirTrevorField()
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field='width_field',
                              height_field='height_field')
    height_field = models.IntegerField(default=0, null=True, blank=True)
    width_field = models.IntegerField(default=0, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    author = models.ForeignKey(User)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    timestamp = models.DateTimeField(db_index=True, auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blogpost-detail', kwargs={'pk': self.id})

class CategoryToPost(models.Model):
    post = models.ForeignKey(BlogPost)
    category = models.ForeignKey(Category)
