import os
from zipfile import ZipFile, ZIP_DEFLATED

from prettytable import PrettyTable

from core import CRAWLAB_TMP
from core.config import config
from core.request import Request


def get_zip_file(input_path, result):
    files = os.listdir(input_path)
    for file in files:
        filepath = os.path.join(input_path, file)
        if os.path.isdir(filepath):
            get_zip_file(filepath, result)
        else:
            result.append(filepath)


def zip_file_path(input_path, target_path):
    f = ZipFile(target_path, 'w', ZIP_DEFLATED)
    file_list = []
    get_zip_file(input_path, file_list)
    for file in file_list:
        f.write(file)
    f.close()
    return target_path


class Client(object):
    def __init__(self):
        pass

    @staticmethod
    def list(columns, items):
        tb = PrettyTable()
        tb.field_names = columns
        for item in items:
            row = []
            for col in columns:
                row.append(item.get(col))
            tb.add_row(row)
        print(tb)
        print(f'total: {len(items)}')

    @staticmethod
    def update_token():
        data = Request.post('/login', data={
            'username': config.data.username,
            'password': config.data.password,
        })
        if data.get('error'):
            print('error: ' + data.get('error'))
            print('error when logging-in')
            return
        config.data.token = data.get('data')
        config.save()
        print('logged-in successfully')

    @staticmethod
    def list_nodes():
        data = Request.get('/nodes')
        if data.get('error'):
            print('error: ' + data.get('error'))
        items = data.get('data') or []
        columns = ['_id', 'name', 'create_ts', 'update_ts']
        Client.list(columns, items)

    @staticmethod
    def list_spiders():
        data = Request.get('/spiders', {'page_size': 99999999})
        if data.get('error'):
            print('error: ' + data.get('error'))
        items = data.get('data').get('list') or []
        columns = ['_id', 'name', 'display_name', 'type', 'col', 'create_ts', 'update_ts']
        Client.list(columns, items)

    @staticmethod
    def list_schedules():
        data = Request.get('/schedules', {'page_size': 99999999})
        if data.get('error'):
            print('error: ' + data.get('error'))
        items = data.get('data') or []
        columns = ['_id', 'name', 'spider_name', 'run_type', 'cron', 'create_ts', 'update_ts']
        Client.list(columns, items)

    @staticmethod
    def list_tasks(number=10):
        data = Request.get('/tasks', {'page_size': number})
        if data.get('error'):
            print('error: ' + data.get('error'))
        items = data.get('data') or []
        columns = ['_id', 'status', 'node_name', 'spider_name', 'error', 'result_count', 'create_ts', 'update_ts']
        Client.list(columns, items)

    @staticmethod
    def upload_customized_spider(directory=None, name=None):
        # check if directory exists
        if not os.path.exists(directory):
            print(f'error: {directory} does not exist')
            return

        # compress the directory to the zipfile
        target_path = os.path.join(CRAWLAB_TMP, name or os.path.basename(directory)) + '.zip'
        zip_file_path(directory, target_path)

        # upload zip file to server
        Request.upload('/spiders', target_path)


client = Client()
