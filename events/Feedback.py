from datetime import datetime
from users.User import *

class Feedback:
    def __init__(self, feedback, client):
        self.id = feedback["id"]
        self.user_login = feedback["user"]['login']
        self.rating = feedback["rating"]
        self.comment = feedback["comment"]
        self.created_at = datetime.strptime(feedback["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.client = client

    def user(self):
        return self.client.UserManager.get_user(self.user_login)

    def toJSON(self):
        return {
            "id": self.id,
            "login": self.user_login,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        }