# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20170404_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenedurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]