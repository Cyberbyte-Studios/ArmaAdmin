import uuid

from django.conf import settings
from django.db import models
from django.utils.timezone import now


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename = models.CharField(max_length=255)
    size = models.IntegerField()
    full_path = models.CharField(max_length=255)
    relative_path = models.CharField(max_length=255)
    hash = models.CharField(max_length=8)
    download = models.URLField()
    created = models.DateTimeField(default=now, editable=False)
    modified = models.DateTimeField(default=now, editable=False)


class FileSync(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    updated = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    previous_total = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    started = models.DateTimeField(default=now, editable=False)
    finished = models.DateTimeField(editable=False, blank=True, null=True)
