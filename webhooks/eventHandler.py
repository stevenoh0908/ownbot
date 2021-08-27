# eventHandler.py
# In here, configuring what happended when you recieve webhook events.

import os, sys, yaml, importlib
import commands.autoGreetings

def chatEventListener(chat):
    if chat.message.strip()[0] == '/':
        command = chat.message.strip().split()[0][1:]
        commands = None
        with open('./commands/config.yml') as config:
            commands = yaml.load(config)['Commands']
            pass
        if command in commands:
            commandScript = importlib.import_module('commands.' + commands[command])
            commandScript.__init__(chat)
        pass
    pass

def nameChangedEventListener(nameChanged):
    pass

def userJoinedEventListener(userJoined):
    pass

def streamStartedEventListener(streamStarted):
    pass

def streamStoppedEventListener(streamStopped):
    pass