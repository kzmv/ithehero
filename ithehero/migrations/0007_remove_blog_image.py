# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-19 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ithehero', '0006_auto_20170316_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]
