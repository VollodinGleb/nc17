# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-02 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20161102_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='language',
            field=models.IntegerField(choices=[(0, 'en'), (1, 'ru'), (2, 'ua')], default=0, help_text='язык'),
        ),
    ]
