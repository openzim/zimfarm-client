import zimfarm
from zimfarm.models import Worker


if __name__ == '__main__':
    username = ''
    password = ''

    zimfarm.login(username, password)
    workers = Worker.list()
    print(workers)
    print([worker.last_heartbeat for worker in workers])
