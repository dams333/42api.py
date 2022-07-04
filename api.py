# By Jmaia

import requests as rq
import json

def get_token(client_id: str, client_secret: str):
    payload = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
    r = rq.post("https://api.intra.42.fr/oauth/token", data=payload)
    r_json = json.loads(r.text)
    try:
        return r_json['access_token']
    except KeyError:
        return "An error occured while getting the token !"

def get_token_from_env():
    with open('.env') as env_file:
        data = json.load(env_file)
        token = get_token(data['CLIENT_ID'], data['CLIENT_SECRET'])
    return token

def get(token: str, path: str):
    headers = {'Authorization': 'Bearer ' + token}
    r = rq.get("https://api.intra.42.fr/" + path, headers=headers)
    return json.loads(r.text)

def print_as_json(text:str):
    print(json.dumps(text, indent=4))