# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0008_joinfriends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinfriends',
            name='email',
        ),
        migrations.RemoveField(
            model_name='joinfriends',
            name='emaill',
        ),
        migrations.RemoveField(
            model_name='joinfriends',
            name='friends',
        ),
        migrations.DeleteModel(
            name='JoinFriends',
        ),
    ]
