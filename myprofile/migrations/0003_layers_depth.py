# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-31 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20171231_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='layers',
            name='depth',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
