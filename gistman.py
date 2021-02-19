import json
import requests


class GistMan:
    def __init__(self, usr_token: str):
        self.access_url = f'https://api.github.com/gists'
        self.req = requests.Session()
        self.req.headers.update({
            'Authorization': f'token {usr_token}',
            'Content-Type': 'application/json'
        })

    def read_gist(self, file_id: str):
        return self.req.get(f'{self.access_url}/{file_id}').json()

    def create_gist(self, file_name: str, content='place holder', public='false'):
        data = {'public': public, 'files': {file_name: {'content': content}}}
        return self.req.post(self.access_url, data=json.dumps(data)).json()

    def update_gist(self, file_id: str, file_name: str, content: str):
        data = {'files': {file_name: {'content': content}}}
        return self.req.patch(f'{self.access_url}/{file_id}', data=json.dumps(data)).json()
