# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='parcel',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='trashpickup',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
