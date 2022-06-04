from typing import Dict, Union


class Spider(dict):
    def __init__(self, value: Dict = None):
        super().__init__(value or {})

    @property
    def name(self) -> Union[str, None]:
        return self.get('name')

    @name.setter
    def name(self, value):
        self['name'] = value

    @property
    def cmd(self) -> Union[str, None]:
        return self.get('cmd')

    @cmd.setter
    def cmd(self, value):
        pass

    @property
    def col_name(self) -> Union[str, None]:
        return self.get('col_name')

    @col_name.setter
    def col_name(self, value):
        self['col_name'] = value
