from datetime import datetime

class Theme:
    def __init__(self, theme, client):
        self.created_at = datetime.strptime(theme['created_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.id = theme['id']
        self.name = theme['name']
        self.updated_at = datetime.strptime(theme['updated_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.client = client

    def toJSON(self):
        return {
            "created_at": self.created_at,
            "id": self.id,
            "name": self.name,
            "updated_at": self.updated_at
        }