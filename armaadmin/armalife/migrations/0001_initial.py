# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.CharField(max_length=17)),
                ('classname', models.CharField(db_column='classname', max_length=32)),
                ('pos', models.CharField(blank=True, max_length=64, null=True)),
                ('inventory', models.TextField()),
                ('gear', models.TextField()),
                ('dir', models.CharField(blank=True, max_length=128, null=True)),
                ('active', models.BooleanField()),
                ('owned', models.NullBooleanField()),
                ('insert_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'containers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('members', models.TextField(blank=True, null=True)),
                ('max_members', models.IntegerField(blank=True, db_column='maxmembers', null=True)),
                ('bank', models.IntegerField(blank=True, null=True)),
                ('active', models.NullBooleanField()),
                ('insert_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'gangs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.CharField(max_length=17)),
                ('pos', models.CharField(blank=True, max_length=64, null=True)),
                ('owned', models.NullBooleanField()),
                ('garage', models.BooleanField()),
                ('insert_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'houses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('aliases', models.TextField()),
                ('pid', models.CharField(max_length=17, unique=True)),
                ('cash', models.IntegerField()),
                ('bankacc', models.IntegerField()),
                ('coplevel', models.CharField(max_length=1)),
                ('mediclevel', models.CharField(max_length=1)),
                ('civ_licenses', models.TextField()),
                ('cop_licenses', models.TextField()),
                ('med_licenses', models.TextField()),
                ('civ_gear', models.TextField()),
                ('cop_gear', models.TextField()),
                ('med_gear', models.TextField()),
                ('civ_stats', models.CharField(max_length=32)),
                ('cop_stats', models.CharField(max_length=32)),
                ('med_stats', models.CharField(max_length=32)),
                ('arrested', models.BooleanField()),
                ('adminlevel', models.CharField(max_length=1)),
                ('donorlevel', models.CharField(max_length=1)),
                ('blacklist', models.BooleanField()),
                ('civ_alive', models.BooleanField()),
                ('civ_position', models.CharField(max_length=64)),
                ('playtime', models.CharField(max_length=32)),
                ('insert_time', models.DateTimeField()),
                ('last_seen', models.DateTimeField()),
            ],
            options={
                'db_table': 'players',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=16)),
                ('name', models.CharField(db_column='classname', max_length=64)),
                ('type', models.CharField(max_length=16)),
                ('pid', models.CharField(max_length=17)),
                ('alive', models.BooleanField()),
                ('blacklist', models.BooleanField()),
                ('active', models.BooleanField()),
                ('plate', models.IntegerField()),
                ('color', models.IntegerField()),
                ('inventory', models.TextField()),
                ('gear', models.TextField()),
                ('fuel', models.FloatField()),
                ('damage', models.CharField(max_length=256)),
                ('insert_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'vehicles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wanted',
            fields=[
                ('id', models.CharField(db_column='wantedID', max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='wantedName', max_length=32)),
                ('crimes', models.TextField(db_column='wantedCrimes')),
                ('bounty', models.IntegerField(db_column='wantedBounty')),
                ('active', models.BooleanField()),
                ('insert_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'wanted',
                'managed': False,
            },
        ),
    ]
