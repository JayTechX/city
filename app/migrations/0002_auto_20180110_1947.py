# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-10 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='message',
            field=models.TextField(max_length=4000),
        ),
    ]
