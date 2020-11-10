import requests
from pprint import pprint
import json
def login(uname, upass):
    details = {'user': uname,
    'password': upass}
    response = requests.post('https://chat-7time.ru/api/v1/login', data=details)
    data = (json.loads(response.text))['data']
    token = (data['authToken'])
    id = (data['me']['_id'])

    return token, id

def channels_list(token, id):
    headers = { 'X-Auth-Token': token,
                'X-User-Id': id,}
    response = requests.get('https://chat-7time.ru/api/v1/groups.list', headers=headers)
    data = (json.loads(response.text))
    gname = []
    gid = []

    for i in range(data['count']):
        gname.append(data['groups'][i]['name'])
        gid.append(data['groups'][i]['_id'])

    return gname, gid, data['count']

def new_user(token, aid, name, email, password, login):
    headers = { 'X-Auth-Token': token,
                'X-User-Id': aid,
                'Content-type': 'application/json',}
    data = {"name": name, "email": email, "password": password, "username": login}
    response = requests.post('https://chat-7time.ru/api/v1/users.create', headers=headers, data=data)
    data = (json.loads(response.text))
    pprint(data)




if __name__ == '__main__':
    pass
