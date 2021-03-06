import os
from datetime import datetime, timedelta
from events.EventManager import *
from users.UserManager import *
from api import *
from dotenv import load_dotenv
load_dotenv()

class Api42Client:
    client_id = ""
    client_secret = ""
    token = ""
    expires_at = 0
    EventManager = None
    UserManager = None

    def __init__(self):
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.token = self.get_token()
        self.expires_at = datetime.now() + timedelta(0, get_token_expire_in(self.token))
        self.EventManager = EventManager(self)
        self.UserManager = UserManager(self)

    def get_token(self):
        if self.expires_at == 0 or self.expires_at < datetime.now():
            self.token = get_token(self.client_id, self.client_secret)
            self.expires_at = datetime.now() + timedelta(0, get_token_expire_in(self.token))
        return self.token