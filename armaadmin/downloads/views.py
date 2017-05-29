from rest_framework import viewsets

from armaadmin.downloads.models import File
from armaadmin.downloads.serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    search_fields = ('id', 'filename', 'size', 'relative_path', 'hash', 'download', 'created', 'branch')
    ordering_fields = ('id', 'filename', 'size', 'relative_path', 'hash', 'download', 'created', 'branch')
    filter_fields = ('id', 'filename', 'size', 'relative_path', 'hash', 'download', 'created', 'branch')
