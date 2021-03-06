# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 21:14
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ithehero', '0010_auto_20170321_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('story', ckeditor.fields.RichTextField()),
                ('info', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
