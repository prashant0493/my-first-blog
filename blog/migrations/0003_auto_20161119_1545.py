# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='Reader',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
