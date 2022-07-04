from api import *
from events.Event import *
from datetime import datetime

class EventManager:
    client = None

    def __init__(self, client):
        self.client = client

    def get_events_by_name(self, campus, name):
        return [Event(event) for event in get(self.client.get_token(), "/v2/events?campus_id=" + str(campus) + "&filter[name]=" + name)]
