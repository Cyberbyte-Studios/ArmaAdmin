# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-29 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import versionfield


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0007_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('version_number', versionfield.VersionField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='downloads.Branch')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='downloads.Branch'),
            preserve_default=False,
        ),
    ]
