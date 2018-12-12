import zimfarm
from zimfarm.models import Worker


if __name__ == '__main__':


    zimfarm.login(username, password)
    workers = Worker.list()
    print(workers)

