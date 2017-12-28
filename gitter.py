import requests
import json


from constants import URL, TOKEN, PAYLOAD, HEADERS


class GitterPy(object):
    def __init__(self):
        pass

    def _get(self, path, query=None):
        self.path = path
        _url = URL+self.path
        _response = requests.get(_url, params=PAYLOAD).json()
        #_response = json.loads(_r.text)
        #_response = json.dumps(_user_data, indent =4, sort_keys=True) # str
        return _response

    def _post(self, path, data):
        _url = URL+path
        self.data = data
        r = requests.post('https://api.gitter.im/v1/rooms/5a3d468fd73408ce4f848340/chatMessages',
		headers=HEADERS, data=self.data)
        return r.status_code

    def get_user(self):
        response = self._get('/user')
        print(type(response), len(response))
        return response

    def get_rooms(self, query=None):
        response = self._get('/rooms')
        return response

    def get_groups(self, query=None):
        response = self._get('/groups')
        return response

    def get_messages(self, query=None):
        response = self._get('/rooms/5a3d468fd73408ce4f848340/chatMessages?limit=8')
        return response

    def post(self, message):
        data = '{}"text":"{}"{}'.format('{', message, '}')
        path = '/rooms/5a3d468fd73408ce4f848340/chatMessages'
        return self._post(path, data)
