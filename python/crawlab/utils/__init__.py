import os

from crawlab.constants import DedupMethod


def get_task_id():
    return os.environ.get('CRAWLAB_TASK_ID')


def get_is_dedup():
    return os.environ.get('CRAWLAB_IS_DEDUP')


def get_dedup_field():
    return os.environ.get('CRAWLAB_DEDUP_FIELD')


def get_dedup_method():
    return os.environ.get('CRAWLAB_DEDUP_METHOD')


def save_item(item):
    try:
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
                col.remove({dedup_field: item[dedup_field]})
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
    except:
        pass
