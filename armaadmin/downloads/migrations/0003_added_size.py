# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-16 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0002_changed_paths'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
