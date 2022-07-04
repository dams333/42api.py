from api import *

def get_events_ids(token: str, name: str):
    return [event['id'] for event in get(token, "/v2/events?campus_id=1&filter[name]=" + name)]

def get_event_users(token: str, event_id: str):
    return get(token, "/v2/events/" + str(event_id) + "/events_users")

def get_event_id(token: str, name: str):
    return get_events_ids(token, name)[0]

def get_event_users_from_name(token: str, name: str):
    return get_event_users(token, get_event_id(token, name))