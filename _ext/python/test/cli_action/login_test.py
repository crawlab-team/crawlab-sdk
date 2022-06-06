import os
import unittest
from argparse import Namespace

from crawlab.cli.actions.login import cli_login
from crawlab.config.config import config


class CliActionLoginTestCase(unittest.TestCase):
    @staticmethod
    def test_login():
        args = Namespace(
            username='admin',
            password='admin',
            api_address=os.environ.get('CRAWLAB_API_ADDRESS') or 'http://localhost:8000'
        )
        cli_login(args)
        assert os.path.exists(config.json_path)
        assert len(config.data.get('token')) > 0


if __name__ == '__main__':
    unittest.main()
