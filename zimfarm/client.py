from typing import Optional
import requests
from requests.auth import AuthBase


class Client:
    base = 'https://farm.openzim.org/api'
    access_token: Optional[str] = None

    def password_auth(self, username: str, password: str):
        response = requests.post(f'{self.base}/auth/oauth2', json={
            'grant_type': 'password',
            'username': username,
            'password': password
        })

        response_json = response.json()
        if response.status_code == 200:
            self.access_token = response_json.get('access_token')
        else:
            raise Exception()

    def get(self, url: str) -> requests.Response:
        return requests.get(f'{self.base}{url}', auth=BearerTokenAuth(self.access_token))


class BearerTokenAuth(AuthBase):
    def __init__(self, access_token: str):
        self.access_token = access_token

    def __call__(self, request):
        request.headers['Authorization'] = f'Bearer {self.access_token}'
        return request
