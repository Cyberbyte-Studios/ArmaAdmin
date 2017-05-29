import uuid

from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import Group

from versionfield import VersionField

class Branch(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    description = models.TextField()
    groups = models.ManyToManyField(Group)

class Version(models.Model):
    name = models.CharField(max_length=255)
    version_number = VersionField()
    branch = models.ForeignKey(Branch)

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename = models.CharField(max_length=255)
    size = models.BigIntegerField()
    full_path = models.CharField(max_length=255)
    relative_path = models.CharField(max_length=255)
    hash = models.CharField(max_length=32)
    download = models.URLField()
    created = models.DateTimeField(default=now, editable=False)
    modified = models.DateTimeField(default=now, editable=False)
    branch = models.ForeignKey(Branch, default=1)

class FileSync(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    updated = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    previous_total = models.IntegerField(blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    started = models.DateTimeField(default=now, editable=False)
    finished = models.DateTimeField(editable=False, blank=True, null=True)

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(default=now)
