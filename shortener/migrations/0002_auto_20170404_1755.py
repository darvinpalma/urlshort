# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=220, unique=True),
        ),
    ]