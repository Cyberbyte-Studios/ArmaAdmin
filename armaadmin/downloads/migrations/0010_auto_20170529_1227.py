# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-29 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0009_auto_20170529_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='downloads.Branch'),
        ),
    ]