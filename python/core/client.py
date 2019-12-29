from prettytable import PrettyTable

from core.config import config
from core.request import Request


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
        print('obtained access token successfully')

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


client = Client()
