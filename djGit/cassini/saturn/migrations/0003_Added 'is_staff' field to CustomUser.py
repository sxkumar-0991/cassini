# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-05 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saturn', '0002_Added Songs table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='Member is Staff'),
        ),
    ]
