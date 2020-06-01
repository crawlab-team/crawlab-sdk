from crawlab.constants import DedupMethod
from crawlab.db.sql import insert_item
from crawlab.utils.config import get_task_id, get_is_dedup, get_dedup_field, get_dedup_method


def save_item_mongo(item):
    from crawlab.db import col

    # 赋值task_id
    item['task_id'] = get_task_id()

    # 是否开启去重
    is_dedup = get_is_dedup()

    if is_dedup == '1':
        # 去重
        dedup_field = get_dedup_field()
        dedup_method = get_dedup_method()
        if dedup_method == DedupMethod.OVERWRITE:
            # 覆盖
            if col.find_one({dedup_field: item[dedup_field]}):
                col.replace_one({dedup_field: item[dedup_field]}, item)
            else:
                col.save(item)
        elif dedup_method == DedupMethod.IGNORE:
            # 忽略
            col.save(item)
        else:
            # 其他
            col.save(item)
    else:
        # 不去重
        col.save(item)


def save_item_sql(item):
    item['task_id'] = get_task_id()
    insert_item(item)
