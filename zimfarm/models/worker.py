from typing import Union
from enum import Enum
from datetime import datetime

from .base import Base


class Status(Enum):
    Online = 'online'
    Offline = 'offline'


class Worker(Base):
    def __init__(self, id: str, hostname: str, status: Union[str, Status], heartbeats: [], **kwargs):
        self.id = id
        self.hostname = hostname
        self.status = Status(status)
        self.heartbeats = heartbeats

    def __repr__(self):
        return f'Worker {self.hostname} {self.status.value}'

    @property
    def last_heartbeat(self):
        return self.heartbeats[-1] if self.heartbeats else None

    @classmethod
    def list(cls) -> ['Worker']:
        response = cls.client.get('/workers/')
        if response.status_code == 200:
            workers = []
            for json in response.json():
                json['id'] = json.pop('_id')
                json['heartbeats'] = [datetime.fromisoformat(json.pop('heartbeat').replace('Z', '+00:00'))]
                worker = cls(**json)
                workers.append(worker)
            return workers
        else:
            raise Exception
