from datetime import datetime

class Waitlist:
    def __init__(self, waitlist, client):
        self.created_at = datetime.strptime(waitlist['created_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.id = waitlist['id']
        self.updated_at = datetime.strptime(waitlist['updated_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.waitlistable_id = waitlist['waitlistable_id']
        self.waitlistable_type = waitlist['waitlistable_type']
        self.client = client