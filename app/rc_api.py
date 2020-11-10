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

    return gname, gid



if __name__ == '__main__':
    token, id = login('testA', 'testAdmin123')
    gname, gid = channels_list(token, id)
    print(gname)
    print(gid)
