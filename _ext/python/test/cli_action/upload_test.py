import os
import tempfile
import unittest
from argparse import Namespace
from datetime import datetime

import requests

from cli.actions.login import login
from cli.actions.upload import upload
from cli.config import config


class CliActionUploadTestCase(unittest.TestCase):
    @staticmethod
    def test_upload():
        dir_path = os.path.join(tempfile.gettempdir(), 'test_spider')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(os.path.join(dir_path, 'main.py'), 'w') as f:
            f.write('print(\'hello world\')')
        os.chdir(dir_path)
        name = 'test_spider' + f'_{int(datetime.now().timestamp())}'
        description = 'test_description_' + f'_{int(datetime.now().timestamp())}'
        cmd = 'echo hello'
        param = 'test'
        args = Namespace(
            id=None,
            dir=None,
            name=name,
            description=description,
            cmd=cmd,
            col_name=None,
            param=param,
            create=True,
        )
        endpoint = os.environ.get('CRAWLAB_API_ADDRESS') or 'http://localhost:8000'
        login(Namespace(
            username='admin',
            password='admin',
            api_address=endpoint,
        ))
        upload(args)

        res = requests.get(f'{endpoint}/spiders', headers={'Authorization': config.data.get("token")},
                           params={'size': 1, 'page': 1, 'sort': '[]'})
        assert res.status_code == 200
        data = res.json().get('data')
        assert len(data) == 1
        spider = data[0]
        assert spider.get('name') == name
        requests.delete(f'{endpoint}/spiders/{spider.get("_id")}')


if __name__ == '__main__':
    unittest.main()
