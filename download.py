import os

import coreapi
import requests
import time

import xxhash

api = "http://localhost:8000/docs/"
client = coreapi.Client()


def get_files():
    schema = client.get(api)
    response = client.action(schema, ["files", "list"])
    print('API provided {count} files'.format(count=response['count']))
    return response['results']


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

    if len(folder_files) > 0:
        for file in files:
            thing = folder_files.pop(file['relative_path'], None)
            if thing is None:
                print('Processing file {name}. Server hash: {server}({server_size}).'.format(name=file['filename'], server=file['hash'], server_size=file['size']))
            else:
                print('Processing file {name}. Server hash: {server}({server_size}). Filesystem hash {file}({file_size})'.format(name=file['filename'], server=file['hash'], file=hash_file(thing), server_size=file['size'], file_size=os.stat(thing).st_size))
            if thing is None or file['hash'] != hash_file(thing):
                download_files.append(file)
    else:
        print('No files exist')

    print('Update {count} files: {files}'.format(count=len(download_files), files=download_files))
    print('Delete {count} files: {files}'.format(count=len(folder_files), files=folder_files))
    for file in download_files:
        download(url=file['download'], path=folder+file['relative_path'])

    for filename, path in folder_files.items():
        print('Removing %s' % path)
        os.remove(path)
        delete_folder(path)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Finished syncing {time}'.format(time=end - start))
