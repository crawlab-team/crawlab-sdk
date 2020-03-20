import os


def get_task_id():
    return os.environ.get('CRAWLAB_TASK_ID')


def save_item(item):
    try:
        from crawlab.db import col
        item['task_id'] = get_task_id()
        col.save(item)
    except:
        pass
