from .base import Base


class Worker(Base):
    def __init__(self, id: str, hostname: str, **kwargs):
        self.id = id
        self.hostname = hostname

    def __repr__(self):
        return f'Worker {self.hostname}'

    @classmethod
    def list(cls) -> ['Worker']:
        response = cls.client.get('/workers/')
        if response.status_code == 200:
            workers = []
            for json in response.json():
                json['id'] = json.pop('_id')
                worker = cls(**json)
                workers.append(worker)
            return workers
        else:
            raise Exception
