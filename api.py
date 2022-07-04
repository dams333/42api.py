# By Jmaia edit by Tbrowang

import requests as rq
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_token(client_id: str, client_secret: str):
    payload = {'grant_type': 'client_credentials', 'client_id':  client_id, 'client_secret': client_secret}
    r = rq.post("https://api.intra.42.fr/oauth/token", data=payload)
    r_json = json.loads(r.text)
    try:
        return r_json['access_token']
    except KeyError:
        return "An error occured while getting the token !"

def get_token_expire_in(token: str):
    return get(token, "oauth/token/info")['expires_in_seconds']

def get(token: str, path: str):
    headers = {'Authorization': 'Bearer ' + token}
    r = rq.get("https://api.intra.42.fr/" + path, headers=headers)
    return json.loads(r.text)