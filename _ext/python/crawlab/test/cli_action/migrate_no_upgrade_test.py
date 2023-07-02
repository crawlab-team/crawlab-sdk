import os
import unittest
from argparse import Namespace

from crawlab.cli.actions.login import cli_login
from crawlab.cli.actions.migrate import cli_migrate
from crawlab.client import get_api_address


class CliActionMigrateNoUpgradeTestCase(unittest.TestCase):
    endpoint = get_api_address()

    def test_migrate_no_upgrade(self):
        cli_login(Namespace(
            username='admin',
            password='admin',
            api_address=self.endpoint,
        ))
        cli_migrate(Namespace(
            api_address=get_api_address(),
            mongo_host='localhost',
            mongo_port=27017,
            mongo_db='crawlab_test',
            mongo_username=None,
            mongo_password=None,
            mongo_auth_source='admin',
            no_upgrade=True,
            source_filer_address='http://localhost:8888',
            target_filer_address='http://demo-pro.crawlab.cn:8888',
        ))


if __name__ == '__main__':
    unittest.main()
