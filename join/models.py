from __future__ import unicode_literals
import os
from django.db import models
from autoslug import AutoSlugField

class job_category(models.Model):
    cat = models.CharField(max_length=50)
    def __str__(self):
        return self.cat

class job_offer(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')
    category = models.ForeignKey(job_category, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True) #automatic publication date
    update_date = models.DateField(auto_now=True) #automatic updation date
    end_date = models.DateField(auto_now_add=False, auto_now=False, null=True, help_text="YYYY-MM-DD") #null equal to true allows optional date
    #add automatic message: format date
    roles_summary = models.TextField()
    responsabilities = models.TextField()
    requirements = models.TextField()
    def __str__(self):
        return '%s\t%s' % (self.title,self.category)

def upload_location(instance, filename):
    return '/uploads/%s/%s' %(instance.id, filename)
      
class uploadcv(models.Model):
    docfile = models.FileField(upload_to=upload_location,null=True, blank=True,)