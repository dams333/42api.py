from api import *
from events.Event import *
from datetime import datetime

class EventManager:
    client = None

    def __init__(self, client):
        self.client = client

    def get_event_by_name(self, campus, name):
        events = get(self.client.get_token(), "/v2/events?campus_id=" + str(campus) + "&filter[name]=" + name)
        if len(events) == 0:
            return None
        return Event(events[0], self.client)
