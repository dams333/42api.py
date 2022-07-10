from api import *
from users.Title import *
from users.Project import *
import json
from datetime import datetime

class User:
    def __init__(self, user_dict, client):
        self.id = user_dict["id"]
        self.email = user_dict["email"]
        self.login = user_dict["login"]
        self.first_name = user_dict["first_name"]
        self.last_name = user_dict["last_name"]
        self.usual_full_name = user_dict["usual_full_name"]
        self.usual_first_name = user_dict["usual_first_name"]
        self.url = user_dict["url"]
        self.phone = user_dict["phone"]
        self.displayname = user_dict["displayname"]
        self.image_url = user_dict["image_url"]
        self.new_image_url = user_dict["new_image_url"]
        self.staff = user_dict["staff?"]
        self.correction_point = user_dict["correction_point"]
        self.pool_month = user_dict["pool_month"]
        self.pool_year = user_dict["pool_year"]
        self.location = user_dict["location"]
        self.wallet = user_dict["wallet"]
        self.anonymize_date = datetime.strptime(user_dict["anonymize_date"], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.data_erasure_date = datetime.strptime(user_dict["data_erasure_date"], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.created_at = datetime.strptime(user_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.updated_at = datetime.strptime(user_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.alumnized_at = datetime.strptime(user_dict["alumnized_at"], "%Y-%m-%dT%H:%M:%S.%f%z") if user_dict["alumnized_at"] != None else None
        self.alumni = user_dict["alumni?"]
        self.client = client

    def titles(self):
        return [Title(title, self.client) for title in get(self.client.get_token(), "/v2/users/" + str(self.id) + "/titles")]

    def projects(self):
        return [Project(project, self.client) for project in get(self.client.get_token(), "/v2/users/" + str(self.id) + "/projects_users?page[size]=100")]

    def get_project(self, slug):
        for project in self.projects():
            if project.slug == slug:
                return project
        return None

    def toJSON(self):
        return {
            "id": self.id,
            "email": self.email,
            "login": self.login,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "usual_full_name": self.usual_full_name,
            "usual_first_name": self.usual_first_name,
            "url": self.url,
            "phone": self.phone,
            "displayname": self.displayname,
            "image_url": self.image_url,
            "new_image_url": self.new_image_url,
            "staff": self.staff,
            "correction_point": self.correction_point,
            "pool_month": self.pool_month,
            "pool_year": self.pool_year,
            "location": self.location,
            "wallet": self.wallet,
            "anonymize_date": self.anonymize_date.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            "data_erasure_date": self.data_erasure_date.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            "alumnized_at": self.alumnized_at.strftime("%Y-%m-%dT%H:%M:%S.%f%z") if self.alumnized_at != None else None,
            "alumni": self.alumni
        }