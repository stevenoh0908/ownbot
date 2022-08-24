import os, requests, json
from requests.structures import CaseInsensitiveDict
from flask import Flask, request, Response, jsonify

BOT_VERSION = '0.0.1'

# read config.json
with open('config.json') as f:
    data_config = json.load(f)
    pass

# init default variables
OWNCAST_URL = data_config['server_url'] + '/api/integrations/chat/send'

# prepare header for the bot posts
headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Bearer ' + data_config['access_token']

# app
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def response():
    params = json.loads(request.get_data(), encoding='utf-8')
    print(params)
    pass

if __name__ == '__main__':
    app.run()
    pass
