# data.py
# owncast webhook return data handler

class User():
    
    userid = None
    displayName = None
    displayColor = None
    createdAt = None
    previousNames = []
    
    def __init__(self, userDict):
        self.userid = userDict['id']
        self.displayName = userDict['displayName']
        self.displayColor = userDict['displayColor']
        self.createdAt = userDict['createdAt']
        self.previousNames = userDict['previousNames']
        pass
    pass

class Chat():
    
    timestamp = None
    user = None
    message = None
    chatid = None
    visible = None

    def __init__(self, chatDict):
        self.timestamp = chatDict['timestamp']
        self.chatid = chatDict['id']
        self.visible = chatDict['visible']
        self.message = chatDict['body']
        self.user = User(chatDict['user'])
        pass
    pass

class NameChanged():
    
    timestamp = None
    user = None
    newName = None

    def __init__(self, namechangedDict):
        self.timestamp = namechangedDict['timestamp']
        self.user = User(namechangedDict['user'])
        self.newName = namechangedDict['newName']
        pass
    pass

class UserJoined():

    timestamp = None
    user = None

    def __init__(self, userjoinedDict):
        self.timestamp = userjoinedDict['timestamp']
        self.user = User(userjoinedDict['user'])
        pass
    pass

class StreamStarted():
    
    name = None
    streamTitle = None
    summary = None
    
    def __init__(self, streamstartedDict):
        self.name = streamstartedDict['name']
        self.streamTitle = streamstartedDict['streamTitle']
        self.summary = streamstartedDict['summary']
        pass
    pass

class StreamStopped():

    name = None
    streamTitle = None
    summary = None

    def __init__(self, streamstoppedDict):
        self.name = streamstoppedDict['name']
        self.streamTitle = streamstoppedDict['streamTitle']
        self.summary = streamstoppedDict['summary']
        pass
    pass
