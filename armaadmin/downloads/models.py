import uuid

from django.db import models
from django.utils.timezone import now


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    hash = models.CharField(max_length=32)
    download = models.URLField()
    created = models.DateTimeField(default=now, editable=False)
