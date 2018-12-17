from typing import Optional

import requests
from requests.auth import AuthBase

from zimfarm.errors import OAuth2Error


class Client:
    base = 'https://farm.openzim.org/api'
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None

    @classmethod
    def password_auth(cls, username: str, password: str) -> (str, str):
        """Authenticate with username and password

        :param username:
        :param password:
        :return access_token, refresh_token: (str, str)
        """

        response = requests.post(f'{cls.base}/auth/oauth2', json={
            'grant_type': 'password',
            'username': username,
            'password': password
        })

        response_json = response.json()
        if response.status_code == 200:
            cls.access_token = response_json.get('access_token')
            cls.refresh_token = response_json.get('access_token')
            return cls.access_token, cls.refresh_token
        else:
            raise OAuth2Error(response_json.get('error'), response_json.get('error_description'))

    def get(self, url: str) -> requests.Response:
        return requests.get(f'{self.base}{url}', auth=BearerTokenAuth(self.access_token))


class BearerTokenAuth(AuthBase):
    def __init__(self, access_token: str):
        self.access_token = access_token

    def __call__(self, request):
        request.headers['Authorization'] = f'Bearer {self.access_token}'
        return request
