import json
from typing import List, Optional

from crawlab.client import get_client, Client
from crawlab.config import get_task_id

from crawlab.entity.result import Result
from crawlab.grpc.entity.stream_message_code_pb2 import INSERT_DATA
from crawlab.grpc.entity.stream_message_pb2 import StreamMessage
from crawlab.grpc.services.task_service_pb2_grpc import TaskServiceStub


class ResultService:
    # internal
    c: Client = None
    task_stub: TaskServiceStub = None

    def __init__(self):
        self.c = get_client()
        self.task_stub = self.c.task_service_stub

    def save_item(self, *items: Result):
        self.save(list(items))

    def save_items(self, items: List[Result]):
        self.save(items)

    def save(self, items: List[Result]):
        _items: List[Result] = []
        for i, item in enumerate(items):
            _items.append(item)
            if i > 0 and i % 50 == 0:
                self._save(_items)
        if len(_items) > 0:
            self._save(_items)

    def _save(self, items: List[Result]):
        # task id
        tid = get_task_id()
        if tid is None:
            return

        records = []
        for item in items:
            item.set_task_id(tid)
            records.append(item)

        data = json.dumps({
            "task_id": tid,
            "records": records,
        }).encode('utf-8')

        msg = self.yield_msg(StreamMessage(
            code=INSERT_DATA,
            data=data,
        ))
        try:
            self.task_stub.Subscribe(msg)
        except Exception as e:
            print(e)
        finally:
            pass

    @staticmethod
    def yield_msg(msg):
        yield msg


RS: Optional[ResultService] = None


def get_result_service() -> ResultService:
    global RS
    if RS is not None:
        return RS
    RS = ResultService()
    return RS


def save_item(*items: Result):
    get_result_service().save_item(*items)


def save_items(items: List[Result]):
    get_result_service().save_items(items)
