import json

class Title:
    def __init__(self, title, client):
        self.id = title["id"]
        self.name = title["name"]
        self.client = client

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name
        }