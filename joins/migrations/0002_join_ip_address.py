# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default='ABC', max_length=120),
        ),
    ]
