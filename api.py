#!/usr/bin/env python3
# By Jmaia edit by Tbrowang

import requests as rq
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_token():
    payload = {'grant_type': 'client_credentials', 'client_id':  os.environ.get("CLIENT_ID"), 'client_secret': os.environ.get("CLIENT_SECRET")}
    r = rq.post("https://api.intra.42.fr/oauth/token", data=payload)
    r_json = json.loads(r.text)
    try:
        return r_json['access_token']
    except KeyError:
        return "An error occured while getting the token !"

def get(token: str, path: str):
    headers = {'Authorization': 'Bearer ' + token}
    r = rq.get("https://api.intra.42.fr/" + path, headers=headers)
    return json.loads(r.text)

def print_as_json(text:str):
    print(json.dumps(text, indent=4))