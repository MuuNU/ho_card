from pprint import pprint
from rocketchat_API.rocketchat import RocketChat

##############################################################
# Login as admin
##############################################################

rocket = RocketChat('testA',
                    'testAdmin123',
                    server_url='https://chat-7time.ru')

##############################################################
# Create New User
# un - username, in which he will login in RocketChat
# bn - First name and last name, which will be showed in chat
# pw - Password
# em - E-Mail adress
##############################################################


def new(un, bn, pw, em):
    pprint(rocket.users_create(em, bn, pw, un).json())


##############################################################
# Add user in chatroom
# uid - User ID
# rid - Room ID
##############################################################


def add(rid, uid):
    pprint(rocket.channels_invite(rid, uid).json())


def list():
    pprint(rocket.channels_list().json())
