from django.contrib import admin

from . import models

admin.site.register(models.job_offer)
admin.site.register(models.job_category)