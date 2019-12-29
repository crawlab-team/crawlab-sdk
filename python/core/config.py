import os
import json
import binascii

PATH = os.path.join(os.environ.get('HOME'), '.crawlab')

if not os.path.exists(PATH):
    os.mkdir(PATH)


class Data(object):
    username = ''
    password = ''
    token = ''
    address = ''

    @property
    def dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'token': self.token,
        }

    @property
    def json(self):
        return json.dumps(self.dict)


class Config(object):
    json_path = os.path.join(PATH, 'config.json')
    data = Data()

    def __init__(self):
        if os.path.exists(self.json_path):
            self.load()
        else:
            self.save()

    def load(self):
        with open(self.json_path) as f:
            data_str = f.read()
            data = json.loads(data_str)
            self.data.username = data.get('username') or ''
            self.data.password = binascii.a2b_hex(data.get('password')).decode()
            self.data.token = data.get('token') or ''

    def save(self):
        data = Data()
        data.username = self.data.username
        data.password = binascii.b2a_hex(self.data.password.encode()).decode()
        data.token = self.data.token
        with open(self.json_path, 'wb') as f:
            f.write(data.json.encode())


# config = Config()
