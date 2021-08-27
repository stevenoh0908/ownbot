# api.py
# owncast api 처리 기본 (chatbot에 필요한 기능만 구현)

from flask import Flask, render_template, request
import requests, json

API_BASIC_URI = 'https://stevenoh0908.kro.kr/live/api'
ACCESS_TOKEN = '9H-HhcE1kr2D4b76wGevnCp_ODRZwpZNb2yWrqKha-Q='
AUTH_ID = 'admin'
AUTH_PASSWD = 'xeno111#'

def get(sub_uri):
    response = requests.get(API_BASIC_URI + sub_uri)
    try:
        return (response.status_code, response.json())
        pass
    except:
        return (response.status_code, None)
        pass
    pass

def postWithAccessToken(sub_uri, payload):
    response = requests.post(API_BASIC_URI + sub_uri, json=payload, headers={'Authorization': 'Bearer ' + ACCESS_TOKEN})
    try:
        return (response.status_code, response.json())
        pass
    except:
        return (response.status_code, None)
        pass
    pass

def postWithAuth(sub_uri, payload):
    response = requests.post(API_BASIC_URI + sub_uri, json=payload, auth=(AUTH_ID, AUTH_PASSWD))
    try:
        return (response.status_code, response.json())
        pass
    except:
        return (response.status_code, None)
        pass
    pass
