import os
import xxhash
from django.utils.encoding import filepath_to_uri

from armaadmin.downloads.models import File


def do_magic(path='/app/armaadmin/static/files'):
    folder_files = hash_folder(path)
    database_files = File.objects.all()
    if len(database_files) > 0:
        exiting_files = []
        for database_file in database_files:
            if folder_files.pop(database_file.hash, None):
                exiting_files.append(database_file.pk)
        File.objects.exclude(pk__in=exiting_files).delete()
    File.objects.bulk_create(folder_files.values())


def hash_folder(folder):
    files = {}
    base_folder_length = len(folder)
    for root, directories, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(root, filename)
            hash = hash_file(path)
            files[hash] = File(
                filename=filename,
                full_path=path,
                relative_path=path[base_folder_length:],
                hash=hash,
                size=filesize(path),
                download='http://localhost:8000/static/files/%s' % filepath_to_uri(path[base_folder_length:]),  # todo: populate based on CDN
            )
    return files


def filesize(path):
    return os.stat(path).st_size


def hash_file(path, block_size=256 * 128):
    hasher = xxhash.xxh32()
    with open(path, 'rb') as file:
        while True:
            buf = file.read(block_size)
            if not buf:
                break
            hasher.update(buf)
    return hasher.hexdigest()
