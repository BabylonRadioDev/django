# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 13:55
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0007_auto_20160817_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_offer',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from=id, unique=True),
        ),
    ]
