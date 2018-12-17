import os


def register(_):
    pass


def process(_):
    print('Logging out...', end='', flush=True)

    try:
        os.remove(os.path.expanduser('~/.zimfarm'))
        print('success')
    except IOError as e:
        print('failure')
        print(f'Error: {e}')
