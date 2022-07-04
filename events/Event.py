from events.Theme import *
from events.Waitlist import *
from datetime import datetime

class Event:
    def __init__(self, event):
      self.id = event['id']
      self.name = event['name']
      self.description = event['description']
      self.location = event['location']
      self.kind = event['kind']
      self.max_people = event['max_people']
      self.nbr_subscribers = event['nbr_subscribers']
      self.begin_at = datetime.strptime(event['begin_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
      self.end_at = datetime.strptime(event['end_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
      self.campus_ids = event['campus_ids']
      self.cursus_ids = event['cursus_ids']
      self.prohibition_of_cancellation = event['prohibition_of_cancellation']
      self.created_at = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
      self.updated_at = datetime.strptime(event["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
      self.theme = []
      for theme in event['themes']:
        self.theme.append(Theme(theme))
      if(event['waitlist'] != None):
        self.waitlist = Waitlist(event['waitlist'])
      else:
        self.waitlist = None