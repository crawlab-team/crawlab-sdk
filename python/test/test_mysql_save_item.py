import json
import os
import unittest

from crawlab import save_item
from crawlab.db.sql import get_conn
from crawlab.utils.config import get_collection, get_dedup_field
from crawlab.constants import DedupMethod

os.environ['CRAWLAB_TASK_ID'] = 'test_task_id'
os.environ['CRAWLAB_COLLECTION'] = 'results2'
os.environ['CRAWLAB_IS_DEDUP'] = '1'
os.environ['CRAWLAB_DEDUP_FIELD'] = 'url'
os.environ['CRAWLAB_DEDUP_METHOD'] = DedupMethod.OVERWRITE
os.environ['CRAWLAB_DATA_SOURCE'] = json.dumps({
    'type': 'mysql',
    'host': 'localhost',
    'port': '3306',
    'database': 'test',
    'username': 'root',
    'password': 'mysql',
})

url = 'example.com'


class MySQLSaveItemTestCase(unittest.TestCase):
    def test_save_item(self):
        for i in range(10):
            save_item({'url': url, 'title': str(i)})
        dedup_field = get_dedup_field()
        table_name = get_collection()
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f'SELECT count(*) FROM {table_name} WHERE {dedup_field} = \'{url}\'')
        conn.commit()
        res = cursor.fetchone()
        assert res[0] == 1
        cursor.execute(f'SELECT url,title FROM {table_name} WHERE {dedup_field} = \'{url}\'')
        conn.commit()
        res = cursor.fetchone()
        assert res[1] == '9'
        cursor.execute(f'DELETE FROM {table_name} WHERE {dedup_field} = \'{url}\'')
        conn.commit()
        cursor.close()


if __name__ == '__main__':
    unittest.main()
