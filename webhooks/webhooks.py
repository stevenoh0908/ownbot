# webhooks.py
# owncast webhook handler based on python Flask

from flask import Flask, render_template, request
import json, datetime

import webhooks.data as data
import webhooks.eventHandler as eventHandler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    # Webhook handler
    if request.method == 'POST':
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        params = json.loads(request.get_data(), encoding='utf-8')
        
        # For Debugging
        if not len(params) == 0:
            params_str = ''
            for key in params.keys():
                params_str += 'key: {}, value: {}\n'.format(key, params[key])
                print(params_str)
                pass
            pass

            webhook_type = params['type']
            webhook_eventData = params['eventData']
            
            if webhook_type == 'CHAT':
                chat = data.Chat(webhook_eventData)
                eventHandler.chatEventListener(chat)
                pass
            elif webhook_type == 'NAME_CHANGE':
                nameChanged = data.NameChanged(webhook_eventData)
                eventHandler.nameChangedEventListener(nameChanged)
                pass
            elif webhook_type == 'USER_JOINED':
                userJoined = data.UserJoined(webhook_eventData)
                eventHandler.userJoinedEventListener(userJoined)
                pass
            elif webhook_type == 'STREAM_STARTED':
                streamStarted = data.StreamStarted(webhook_eventData)
                eventHandler.streamStartedEventListener(streamStarted)
                pass
            elif webhook_type == 'STREAM_STOPPED':
                streamStopped = data.StreamStopped(webhook_eventData)
                eventHandler.streamStoppedEventListener(streamStopped)
                pass
            
            return ''
            pass
        pass
    pass

def start():
    app.run(host='127.0.0.1', port=9001, debug=True)
    pass
