import zimfarm
from zimfarm.models import Worker


if __name__ == '__main__':
    username = ''
    password = ''

    zimfarm.login(username, password)
    workers = Worker.list()
    print(workers)

    for worker in workers:
        # username@node_name
        hostname = worker.hostname

        # online, offline or unknown
        status = worker.status

        # a datetime object
        last_heartbeat = worker.last_heartbeat
