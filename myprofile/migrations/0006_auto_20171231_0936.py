# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-31 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0005_auto_20171231_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layers',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profilelayer_set', to='myprofile.Profile'),
        ),
    ]
