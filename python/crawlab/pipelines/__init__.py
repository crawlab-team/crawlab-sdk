import os

from crawlab.db import col

TASK_ID = os.environ.get('CRAWLAB_TASK_ID')


class CrawlabMongoPipeline(object):
    def process_item(self, item, spider):
        item_dict = dict(item)
        item_dict['task_id'] = TASK_ID
        col.save(item_dict)

        return item
