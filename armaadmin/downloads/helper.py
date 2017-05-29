import os
import xxhash
from multiprocessing.pool import ThreadPool

from django.db import transaction
from django.db.models import Sum
from django.utils import timezone
from django.utils.encoding import filepath_to_uri

from armaadmin.downloads.models import File, FileSync

def start(path='', user=None):
    path = '/app/armaadmin/static/files'
    job = FileSync(user=user)
    job.save()

    files = {}
    folder = hash_folder(path)
    for file in folder:
        files[file.relative_path] = file

    database_files = File.objects.all()
    job.previous_total = database_files.count()
    stats = update_files(files, database_files)

    print(stats)
    job.created = stats['created']
    job.updated = stats['updated']
    job.deleted = stats['deleted']
    job.total = File.objects.all().count()
    job.size = File.objects.aggregate(Sum('size'))['size__sum'] or 0
    job.finished = timezone.now()
    job.save()
    return job


@transaction.atomic
def update_files(folder_files, database_files):
    loose_files = []
    stats = {'created': 0, 'updated': 0, 'deleted': 0}
    for database_file in database_files:
        file = folder_files.pop(database_file.relative_path, None)
        if file is not None:
            if file.hash != database_file.hash or file.size != database_file.size:
                database_file.hash = file.hash
                database_file.size = file.size
                database_file.download = file.download
                database_file.full_path = file.full_path
                database_file.modified = file.modified
                database_file.save()
                stats['updated'] += 1
        else:
            loose_files.append(database_file.pk)
    stats['deleted'] = File.objects.filter(pk__in=loose_files).delete()[0]
    stats['created'] = len(File.objects.bulk_create(folder_files.values()))
    return stats


def create_file(full_path, relative_path, filename):
    return File(
        filename=filename,
        full_path=full_path,
        relative_path=relative_path,
        hash=hash_file(full_path),
        size=filesize(full_path),
        download='http://localhost:8000/static/files/%s' % filepath_to_uri(relative_path),
    #     todo: populate based on CDN
    )


def hash_folder(folder):
    hasher_pool = ThreadPool(4)
    files = hasher_pool.starmap(create_file, get_files_in_folder(folder))
    hasher_pool.close()
    hasher_pool.join()
    return files


def get_files_in_folder(folder):
    base_folder_length = len(folder)
    file_paths = []
    for root, directories, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(root, filename)
            file_paths.append((path, path[base_folder_length:], filename))
    return file_paths


def filesize(path):
    return os.stat(path).st_size


def hash_file(path, block_size=256 * 128):
    hasher = xxhash.xxh64()
    with open(path, 'rb') as file:
        while True:
            buf = file.read(block_size)
            if not buf:
                break
            hasher.update(buf)
    return hasher.hexdigest()
