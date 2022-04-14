import json

import elasticsearch as elasticsearch

from crawlab.utils.config import get_data_source


def get_client() -> elasticsearch.Elasticsearch:
    ds = get_data_source()
    base_auth = None
    if ds.get('username') is not None and ds.get('password') is not None:
        base_auth = f'{ds.get("username")}:{ds.get("password")}'
    return elasticsearch.Elasticsearch(
        hosts=[{'host': ds.get('host'), 'port': ds.get('port')}],
        basic_auth=base_auth,
    )


def index_item(item):
    ds = get_data_source()
    client = get_client()
    client.index(
        index=ds.get('database'),
        body=item,
    )
