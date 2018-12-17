import json
import os
from argparse import ArgumentParser, Namespace

from zimfarm.client import Client
from zimfarm.errors import OAuth2Error


def register(parser: ArgumentParser):
    parser.add_argument('username', type=str, help='a valid Zimfarm username')
    parser.add_argument('password', type=str, help='a valid Zimfarm password')


def process(args: Namespace):
    username, password = args.username, args.password

    print('Logging in...', end='', flush=True)
    try:
        # auth using username and password
        access_token, refresh_token = Client.password_auth(username, password)

        # write zimfarm profile to home dir
        profile = {'access_token': access_token, 'refresh_token': refresh_token}
        with open(os.path.expanduser('~/.zimfarm'), 'w+') as file:
            json.dump(profile, file)

        print('success')
    except OAuth2Error as e:
        print('failure')

        print(f'Error: {e.error}')
        print(f'Description: {e.description}')
    except FileNotFoundError as e:
        print('failure')
        print(e)
