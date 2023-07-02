import json
import os
import tempfile
from datetime import datetime

import requests

from crawlab.errors.upload import HttpException

from crawlab.actions.upload import exists_spider_by_name, create_spider, upload_file, is_ignored
from print_color import print as print_color

from crawlab.actions.migrate import get_spiders


def migrate_no_upgrade(mongo_db=None, source_filer_address=None, target_filer_address=None):
    print_color('start migrating', tag='info', tag_color='cyan', color='white')

    # mongo spiders collection
    mongo_col_spiders = mongo_db.spiders

    # spiders
    spiders = get_spiders(mongo_col_spiders)
    print_color(f'found {len(spiders)} spiders', tag='info', tag_color='cyan', color='white')

    # stats
    stats = {
        'success': 0,
        'error': 0,
        'skipped': 0,
    }

    # iterate spiders
    for spider in spiders:
        # download files
        dir_path = _download_spider_files(str(spider['_id']), source_filer_address, target_filer_address)
        print(dir_path)
        print(os.listdir(dir_path))
        continue

        # migrated spider name
        migrated_spider_name = f'{spider["name"]}_{spider["_id"]}'

        # create spider if not exists
        if exists_spider_by_name(migrated_spider_name):
            print_color(f'spider "{spider["name"]}" already migrated', tag='info', tag_color='cyan', color='white')
            stats['skipped'] += 1
            continue

        try:
            spider_id = create_spider(name=migrated_spider_name,
                                      description=f'migrated from older version {datetime.now()}')
            print_color(f'created spider {spider["name"]} (id: {spider_id})', tag='success', tag_color='green',
                        color='white')
        except HttpException:
            print_color(f'create spider {spider["name"]} failed', tag='error', tag_color='red', color='white')
            stats['error'] += 1
            return

        # upload spider files to api
        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                # file path
                file_path = os.path.join(root, file_name)

                # ignored file
                if is_ignored(file_path):
                    continue

                # target path
                target_path = file_path.replace(dir_path, '')

                # upload file
                upload_file(spider_id, file_path, target_path)

        stats['success'] += 1

        # spider logging
        print_color(f'uploaded spider {spider["name"]}', tag='success', tag_color='green', color='white')

    # logging
    print_color(f'migration finished', tag='info', tag_color='cyan', color='white')
    print_color(f'success: {stats["success"]}', tag='info', tag_color='cyan', color='white')
    print_color(f'failed: {stats["error"]}', tag='info', tag_color='cyan', color='white')
    print_color(f'skipped: {stats["skipped"]}', tag='info', tag_color='cyan', color='white')


def _download_spider_files(spider_id: str, source_filer_address: str, target_filer_address: str) -> str:
    tmp_dir = tempfile.gettempdir()
    root_dir = os.path.join(tmp_dir, spider_id)
    os.makedirs(root_dir, exist_ok=True)

    path = f'fs/{spider_id}'
    _download_file(path, root_dir, source_filer_address, target_filer_address)

    return root_dir


def _download_file(path: str, root_dir: str, source_filer_address: str, target_filer_address: str):
    url = f'{source_filer_address}/{path}'
    res = requests.get(
        url=url,
        headers={
            'Accept': 'application/json',
        },
    )
    data = json.loads(res.content)

    for e in data.get('Entries'):
        # dir
        if e.get('chunks') is None:
            pass
        # file
        else:
            res = requests.get(f'{source_filer_address}{e.get("FullPath")}')
            file_path = e.get('FullPath').replace(path, root_dir)
            with open(file_path, 'wb') as f:
                f.write(res.content)
