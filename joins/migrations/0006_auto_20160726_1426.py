# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0005_auto_20160726_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='ABC', max_length=120, unique=True),
        ),
    ]
