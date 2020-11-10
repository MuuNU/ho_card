import requests
from pprint import pprint
import json
def login():
    data = {'user': 'testA',
    'password': 'testAdmin123'}
    response = requests.post('https://chat-7time.ru/api/v1/login', data=data)
    data = (json.loads(response.text))['data']
    pprint(data['authToken'])
    pprint(data['me']['_id'])


if __name__ == '__main__':
    login()
