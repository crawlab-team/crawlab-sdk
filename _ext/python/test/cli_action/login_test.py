import os
import unittest
from argparse import Namespace

from cli.actions.login import login
from cli.config import config


class CliActionLoginTestCase(unittest.TestCase):
    @staticmethod
    def test_login():
        args = Namespace(
            username='admin',
            password='admin',
            api_address=os.environ.get('CRAWLAB_API_ADDRESS') or 'http://localhost:8000'
        )
        login(args)
        assert os.path.exists(config.json_path)
        assert len(config.data.get('token')) > 0


if __name__ == '__main__':
    unittest.main()
