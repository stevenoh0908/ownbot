import os, requests, json
from requests.structures import CaseInsensitiveDict
from flask import Flask, request, Response, jsonify

BOT_VERSION = '0.0.1'

# read config.json
with open('config.json') as f:
    data_config = json.load(f)
    pass
# read commands.json
with open('commands.json') as f:
    commands = json.load(f)
    pass

# init default variables
OWNCAST_URL = data_config['server_url'] + '/api/integrations/chat/send'

# prepare header for the bot posts
headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Bearer ' + data_config['access_token']

def sendChat(message):
    resp = requests.post(OWNCAST_URL, headers = headers, data=('{"body":"' + message + '"}').encode('utf-8'))
    return resp.status_code

# app
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def response():
    params = json.loads(request.get_data())
    if params['type'] == 'CHAT' and params['eventData']['body'] in commands:
        resp = sendChat(commands[params['eventData']['body']])
        print(resp)
        pass
    return Response(status=200)

if __name__ == '__main__':
    app.run()
    pass
