from crawlab.constants import DataSourceType
from crawlab.utils.config import get_data_source_type
from crawlab.utils.data import save_item_mongo, save_item_sql, save_item_kafka


def save_item(item):
    try:
        if get_data_source_type() == DataSourceType.MONGO:
            save_item_mongo(item)
        elif get_data_source_type() == DataSourceType.KAFKA:
            save_item_kafka(item)
        else:
            save_item_sql(item)
    except Exception as ex:
        print(ex)
        pass
