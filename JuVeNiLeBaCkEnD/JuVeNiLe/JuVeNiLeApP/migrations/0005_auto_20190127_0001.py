# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-27 00:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JuVeNiLeApP', '0004_auto_20190126_2355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lostandfoundrecords',
            old_name='imageOfChild1',
            new_name='imageOfChild',
        ),
    ]
