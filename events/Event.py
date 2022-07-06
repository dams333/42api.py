from events.Theme import *
from events.Waitlist import *
from users.User import *
from datetime import datetime
from api import *

class Event:
	def __init__(self, event, client):
		self.client = client
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
			self.theme.append(Theme(theme, self.client))
		if(event['waitlist'] != None):
			self.waitlist = Waitlist(event['waitlist'], self.client)
		else:
			self.waitlist = None
  
	def users(self):
		return [User(user['user'], self.client) for user in get(self.client.get_token(), "v2/events/" + str(self.id) + "/events_users")]
