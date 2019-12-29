import json

import requests
from core.config import config


class Request(object):
    @staticmethod
    def get_error(res):
        try:
            return json.loads(res.content)
        except Exception as err:
            print(err)
            return None

    @staticmethod
    def get(path, params=None):
        res = requests.get(
            f'{config.data.api_address}{path}',
            params,
            headers={'Authorization': config.data.token},
        )
        if res.status_code != 200:
            return Request.get_error(res)
        return json.loads(res.content)

    @staticmethod
    def post(path, data=None):
        res = requests.post(
            f'{config.data.api_address}{path}',
            json=data,
            headers={'Authorization': config.data.token},
        )
        if res.status_code != 200:
            return Request.get_error(res)
        return json.loads(res.content)

    @staticmethod
    def put(path, data=None):
        res = requests.put(
            f'{config.data.api_address}{path}',
            json=data,
            headers={'Authorization': config.data.token},
        )
        if res.status_code != 200:
            return Request.get_error(res)
        return json.loads(res.content)

    @staticmethod
    def delete(path=None):
        res = requests.delete(
            f'{config.data.api_address}{path}',
            headers={'Authorization': config.data.token},
        )
        if res.status_code != 200:
            return Request.get_error(res)
        return json.loads(res.content)

    @staticmethod
    def upload(path=None, file=None):
        res = requests.post(
            f'{config.data.api_address}{path}',
            headers={'Authorization': config.data.token},
            files={
                'file': open(file, 'rb')
            }
        )
        if res.status_code != 200:
            return Request.get_error(res)
        return json.loads(res.content)
