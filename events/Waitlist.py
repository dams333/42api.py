from datetime import datetime

class Waitlist:
    def __init__(self, waitlist, client):
        self.created_at = datetime.strptime(waitlist['created_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.id = waitlist['id']
        self.updated_at = datetime.strptime(waitlist['updated_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.waitlistable_id = waitlist['waitlistable_id']
        self.waitlistable_type = waitlist['waitlistable_type']
        self.client = client

    def toJSON(self):
        return {
            "created_at": self.created_at,
            "id": self.id,
            "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            "waitlistable_id": self.waitlistable_id,
            "waitlistable_type": self.waitlistable_type
        }