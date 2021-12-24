import os
import re

from print_color import print as print_color

from cli.client.request import http_put, http_post
from cli.constants import CLI_DEFAULT_UPLOAD_IGNORE_PATTERNS, CLI_DEFAULT_UPLOAD_SPIDER_MODE
from cli.errors import MissingIdException, HttpException


def upload(args):
    # spider id
    _id = args.id

    # dir
    dir_ = args.dir
    if dir_ is None:
        dir_ = os.path.abspath('.')

    # name
    name = args.name
    if name is None:
        name = os.path.basename(dir_)

    # create spider
    if args.create:
        try:
            _id = create_spider(name=name, col_name=args.col_name, cmd=args.cmd)
            print_color(f'created spider {name} (id: {_id})', tag='success', tag_color='green', color='white')
        except HttpException:
            print_color(f'create spider {name} failed', tag='error', tag_color='red', color='white')
            return

    # stats
    stats = {
        'success': 0,
        'error': 0,
    }

    # iterate files
    for root, dirs, files in os.walk(dir_):
        for file_name in files:
            # file path
            file_path = os.path.join(root, file_name)

            # ignored file
            if is_ignored(file_path):
                continue

            # target path
            target_path = file_path.replace(dir_, '')

            # upload file
            try:
                upload_file(_id, file_path, target_path)
                print_color(f'uploaded {file_path}', tag='success', tag_color='green', color='white')
                stats['success'] += 1

            except HttpException:
                print_color(f'failed to upload {file_path}', tag='error', tag_color='red', color='white')
                stats['error'] += 1

    # logging
    print_color(f'uploaded spider {name}', tag='success', tag_color='green', color='white')
    print_color(f'success: {stats["success"]}', tag='info', tag_color='cyan', color='white')
    print_color(f'failed: {stats["error"]}', tag='info', tag_color='cyan', color='white')


def create_spider(name: str, col_name: str = None, cmd: str = None) -> str:
    # results collection name
    if col_name is None:
        col_name = f'results_{name}'

    # http put
    res = http_put(url='/spiders', data={
        'name': name,
        'mode': CLI_DEFAULT_UPLOAD_SPIDER_MODE,
        'col_name': col_name,
        'cmd': cmd,
    })

    return res.json().get('data').get('_id')


def upload_file(_id: str, file_path: str, target_path: str):
    if _id is None:
        raise MissingIdException

    with open(file_path, 'rb') as f:
        data = {
            'path': target_path,
        }
        files = {'file': f}

        url = f'/spiders/{_id}/files/save'
        http_post(url=url, data=data, files=files, headers={})


def is_ignored(file_path: str) -> bool:
    for pat in CLI_DEFAULT_UPLOAD_IGNORE_PATTERNS:
        if re.search(pat, file_path) is not None:
            return True
    return False
