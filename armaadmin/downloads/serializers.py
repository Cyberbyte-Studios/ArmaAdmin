from rest_framework import serializers

from armaadmin.downloads.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'filename', 'size', 'relative_path', 'hash', 'download', 'created')
