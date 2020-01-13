from crawlab.db import col
from crawlab.utils import get_task_id


class CrawlabMongoPipeline(object):
    def process_item(self, item, spider):
        item_dict = dict(item)
        item_dict['task_id'] = get_task_id()
        col.save(item_dict)

        return item
