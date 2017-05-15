import os

import coreapi
import requests
import time
import xxhash

from multiprocessing.dummy import Pool as ThreadPool

api = "http://localhost:8000/docs/"
client = coreapi.Client()
threads = 4

def get_files():
    schema = client.get(api)
    response = client.action(schema, ["files", "list"])
    print('API provided {count} files'.format(count=response['count']))
    return response['results']


def download_file(file):
    download(url=file['download'], path='/home/scollins/projects/armaadmin/files2'+file['relative_path'])

def delete_file(path):
    relative_path, full_path = path
    print('Removing %s' % full_path)
    os.remove(full_path)
    delete_folder(full_path)

def download(url, path):
    print('Downloading from %s' % url)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    r.close()
    return path


def delete_folder(path):
    folder = os.path.dirname(path)
    if len(os.listdir(folder)) is 0:
        print('Removing empty folder %s' % folder)
        os.rmdir(folder)
        delete_folder(folder)
    return folder


def hash_file(path, block_size=256 * 128):
    hasher = xxhash.xxh32()
    with open(path, 'rb') as file:
        while True:
            buf = file.read(block_size)
            if not buf:
                break
            hasher.update(buf)
    return hasher.hexdigest()


def main():
    files = get_files()
    download_files = []

    folder = '/home/scollins/projects/armaadmin/files2'
    folder_files = {}
    base_folder_length = len(folder)

    for root, directories, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(root, filename)
            folder_files[path[base_folder_length:]] = path

    for file in files:
        thing = folder_files.pop(file['relative_path'], None)
        if thing is None or file['hash'] != hash_file(thing):
            download_files.append(file)

    print('Update {count} files: {files}'.format(count=len(download_files), files=download_files))
    print('Delete {count} files: {files}'.format(count=len(folder_files), files=folder_files))

    download_pool = ThreadPool(threads)
    download_pool.map(download_file, download_files)
    download_pool.close()
    download_pool.join()

    delete_pool = ThreadPool(threads)
    delete_pool.map(delete_file, folder_files.items())
    delete_pool.close()
    delete_pool.join()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Finished syncing {time}'.format(time=end - start))
