# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_reportunit_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportunit',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
