import elasticsearch as elasticsearch

from crawlab.utils.config import get_data_source


def get_client() -> elasticsearch.Elasticsearch:
    ds = get_data_source()
    http_auth = None
    if ds.get('username') is not None and ds.get('password') is not None:
        http_auth = f'{ds.get("username")}:{ds.get("password")}'
    return elasticsearch.Elasticsearch(
        hosts=[{
            'host': ds.get('host'),
            'port': ds.get('port'),
            'http_auth': http_auth,
        }],
    )


def index_item(item):
    ds = get_data_source()
    client = get_client()
    client.index(
        index=ds.get('database'),
        body=item,
    )
