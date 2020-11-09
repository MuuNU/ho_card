import requests
import json
import pprint
data = {
  'user': 'testA',
  'password': 'testAdmin123'
}
response = requests.post('https://chat-7time.ru/api/v1/login', data=data)
pprint.pprint(response)
