# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0007_auto_20160726_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Sharer', to='joins.Join')),
                ('emaill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Emaill', to='joins.Join')),
                ('friends', models.ManyToManyField(blank=True, null=True, related_name='Friend', to='joins.Join')),
            ],
        ),
    ]