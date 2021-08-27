# app.py

from flask import Flask, render_template, request
import requests, json

API_BASIC_URI = 'https://stevenoh0908.kro.kr/live/api/'
ACCESS_TOKEN = '9H-HhcE1kr2D4b76wGevnCp_ODRZwpZNb2yWrqKha-Q='
HEAD = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
AUTH_ID = 'admin'
AUTH_PASSWD = 'xeno111#'

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    # Webhook handler
    if request.method == 'POST':
        params = json.loads(request.get_data(), encoding='utf-8')
        if not len(params) == 0:
            params_str = ''
            for key in params.keys():
                params_str += 'key: {}, value: {}\n'.format(key, params[key])
                print(params_str)
                pass
            pass

            webhook_type = params['type']
            webhook_eventData = params['eventData']

            timestamp = webhook_eventData['timestamp']

            if webhook_type == 'CHAT':
                username = webhook_eventData['user']['displayName']
                message = webhook_eventData['body']
                log(timestamp, "username %s said: %s" % (username, message))
                if message.split()[0] == '/syschat':
                    sendSysChat(message.split()[1])
                    pass
                if message.split()[0] == '/title':
                    changeStreamtitle(message.split()[1])
                    pass
                pass
            elif webhook_type == 'NAME_CHANGE':
                userid = webhook_eventData['user']['id']
                previousNames = webhook_eventData['user']['previousNames']
                newName = webhook_eventData['newName']
                log(timestamp, "userid %s, previously known as %s is known as %s from now on." % (userid, previousNames[-1], newName))
                pass
            elif webhook_type == 'USER_JOINED':
                userid = webhook_eventData['user']['id']
                username = webhook_eventData['user']['displayName']
                log(timestamp, "userid %s, known as %s just joined stream!" % (userid, username))
                pass
            elif webhook_type == 'STREAM_STARTED':
                name = webhook_eventData['name']
                streamTitle = webhook_eventData['streamTitle']
                summary = webhook_eventData['summary']
                log(timestamp, "%s just has started stream, with title as %s and summary as %s!" % (name, streamTitle, summary))
                pass
            elif webhook_type == 'STREAM_STOPPED':
                name = webhook_eventData['name']
                streamTitle = webhook_eventData['streamTitle']
                summary = webhook_eventData['summary']
                log(timestamp, "%s just has stopped stream, with title as %s and summary as %s!" % (name, streamTitle, summary))
                pass
            pass
        pass
    return ''
    pass

def sendSysChat(message):
    API_URI = API_BASIC_URI + '/integrations/chat/system'
    payload = {"body": str(message)}
    response = requests.post(API_URI, json=payload, headers=HEAD)
    print(response.json()['success'])
    pass

def changeStreamtitle(title):
    API_URI = API_BASIC_URI + '/admin/config/streamtitle'
    payload = {"value": str(title)}
    response = requests.post(API_URI, json=payload, auth=(AUTH_ID, AUTH_PASSWD))
    print(response.json()['success'])
    pass

def log(timestamp, string):
    print("[%s %s] %s" % (timestamp.split('T')[0], timestamp.split('T')[-1].split('.')[0], string))
    pass

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9001, debug=True)
    pass
