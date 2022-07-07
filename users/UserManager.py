from api import *
from datetime import datetime
from users.User import *

class UserManager:
    client = None

    def __init__(self, client):
        self.client = client

    def get_user(self, login):
        users = get(self.client.get_token(), "/v2/users?filter[login]=" + login)
        if(len(users) == 0):
            return None
        return User(users[0], self.client)
