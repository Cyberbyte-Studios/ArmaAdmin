from django.db import models


class Player(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    aliases = models.TextField()
    pid = models.CharField(unique=True, max_length=17)
    cash = models.IntegerField()
    bankacc = models.IntegerField()
    coplevel = models.CharField(max_length=1)
    mediclevel = models.CharField(max_length=1)
    civ_licenses = models.TextField()
    cop_licenses = models.TextField()
    med_licenses = models.TextField()
    civ_gear = models.TextField()
    cop_gear = models.TextField()
    med_gear = models.TextField()
    civ_stats = models.CharField(max_length=32)
    cop_stats = models.CharField(max_length=32)
    med_stats = models.CharField(max_length=32)
    arrested = models.BooleanField()
    adminlevel = models.CharField(max_length=1)
    donorlevel = models.CharField(max_length=1)
    blacklist = models.BooleanField()
    civ_alive = models.BooleanField()
    civ_position = models.CharField(max_length=64)
    playtime = models.CharField(max_length=32)
    insert_time = models.DateTimeField()
    last_seen = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'players'


class Container(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.CharField(max_length=17)
    classname = models.CharField(db_column='classname', max_length=32)
    pos = models.CharField(max_length=64, blank=True, null=True)
    inventory = models.TextField()
    gear = models.TextField()
    dir = models.CharField(max_length=128, blank=True, null=True)
    active = models.BooleanField()
    owned = models.NullBooleanField()
    insert_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'containers'
        unique_together = (('id', 'pid'),)


class Gang(models.Model):
    owner = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(unique=True, max_length=32, blank=True, null=True)
    members = models.TextField(blank=True, null=True)
    max_members = models.IntegerField(db_column='maxmembers', blank=True, null=True)
    bank = models.IntegerField(blank=True, null=True)
    active = models.NullBooleanField()
    insert_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gangs'


class House(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.CharField(max_length=17)
    pos = models.CharField(max_length=64, blank=True, null=True)
    owned = models.NullBooleanField()
    garage = models.BooleanField()
    insert_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'houses'
        unique_together = (('id', 'pid'),)


class Vehicle(models.Model):
    side = models.CharField(max_length=16)
    name = models.CharField(db_column='classname', max_length=64)
    type = models.CharField(max_length=16)
    pid = models.CharField(max_length=17)
    alive = models.BooleanField()
    blacklist = models.BooleanField()
    active = models.BooleanField()
    plate = models.IntegerField()
    color = models.IntegerField()
    inventory = models.TextField()
    gear = models.TextField()
    fuel = models.FloatField()
    damage = models.CharField(max_length=256)
    insert_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehicles'


class Wanted(models.Model):
    id = models.CharField(db_column='wantedID', primary_key=True, max_length=64)
    name = models.CharField(db_column='wantedName', max_length=32)
    crimes = models.TextField(db_column='wantedCrimes')
    bounty = models.IntegerField(db_column='wantedBounty')
    active = models.BooleanField()
    insert_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wanted'
