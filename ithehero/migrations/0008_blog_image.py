# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-19 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ithehero', '0007_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/noimage.jpg', upload_to='images'),
        ),
    ]
