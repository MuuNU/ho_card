import requests
from pprint import pprint
import json
def login(uname, upass):
    details = {'user': uname,
                'password': upass}
    response = requests.post('https://muunull.rocket.chat/api/v1/login', data=details)
    data = (json.loads(response.text))['data']
    token = (data['authToken'])
    id = (data['me']['_id'])
    print(token)
    print(id)
    return token, id

def channels_list(token, id):
    headers = { 'X-Auth-Token': token,
                'X-User-Id': id,}
    response = requests.get('https://muunull.rocket.chat/api/v1/groups.list', headers=headers)
    data = (json.loads(response.text))
    gname = []
    gid = []

    for i in range(data['count']):
        gname.append(data['groups'][i]['name'])
        gid.append(data['groups'][i]['_id'])

    return gname, gid, data['count']

def new_user(token, aid, name, eml, password, lgn):
    headers = { 'X-Auth-Token': token,
                'X-User-Id': aid,
                'Content-type': 'application/json',}
    data = json.dumps({"name": name, "email": eml, "password": password, "username": lgn, "joinDefaultChannels": False, "verified": True})
    response = requests.post('https://muunull.rocket.chat/api/v1/users.create', headers=headers, data=data)
    id = (json.loads(response.text))['user']['_id']
    username = (json.loads(response.text))['user']['username']
    return id, username

def add_to_groups(token, aid,group_list, uid):
    i = 0
    for e in group_list:
        headers = { 'X-Auth-Token': token,
                    'X-User-Id': aid,
                    'Content-type': 'application/json',}
        data = json.dumps({"roomId": e, "userId": uid})
        print(e)
        response = requests.post('https://muunull.rocket.chat/api/v1/groups.invite', headers=headers, data=data)
        pprint(json.loads(response.text))

if __name__ == '__main__':
    token, id = login('admin', '19852001Ff')
    new_user(token, id, 'Test Test', 'email@7-time.ru', 'password123', 'testTtt')
