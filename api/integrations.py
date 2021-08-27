# integrations.py
# Integrations API 관리

import owncast_api as api

# Integrations - Set the stream title
def setStreamtitle(title):
    __status_code, __response = api.postWithAccessToken('/integrations/streamtitle', {
        'value': title
    })
    if __status_code == 200:
        return __response['success']
        pass
    else:
        return False
        pass
    pass

# Integrations - Send a chat message
def sendChat(message):
    __status_code, __response = api.postWithAccessToken('/integrations/chat/send', {
        'body': message
    })
    if __status_code == 200:
        return __response['success']
        pass
    else:
        return False
        pass
    pass

# Integrations - Send a system chat message
def sendSystemChat(message):
    __status_code, __response = api.postWithAccessToken('/integrations/chat/system', {
        'body': message
    })
    if __status_code == 200:
        return __response['success']
        pass
    else:
        return False
        pass
    pass

# Integrations - Send a chat action
def sendChatAction(username, message):
    __status_code, __response = api.postWithAccessToken('/integrations/chat/action', {
        'body': message,
        'author': username
    })
    if __status_code == 200:
        return __response['success']
        pass
    else:
        return False
        pass
    pass

# Integrations - Update the visiblity of chat messages
def updateMessageVisibility(chatids, visible):
    __status_code, __response = api.postWithAccessToken('/integrations/chat/updatemessagevisibility',
    {
        "visible": visible,
        "idArray": chatids
    })
    if __status_code == 200:
        return __response['success']
        pass
    else:
        return False
        pass
    pass

class User():

    connectedAt = None
    messageCount = None
    userAgent = None
    geo = None
    userid = None
    displayName = None
    displayColor = None
    createdAt = None
    previousNames = None
    nameChangedAt = None

    def __init__(self, userDict):
        self.connectedAt = userDict['connectedAt']
        self.messageCount = userDict['messageCount']
        if userDict['geo']:
            self.geo = userDict['geo']['countryCode'] + '-' + userDict['geo']['regionName'] + '-' + userDict['geo']['timeZone']
            pass
        self.userAgent = userDict['userAgent']
        self.userid = userDict['user']['id']
        self.displayName = userDict['user']['displayName']
        self.displayColor = userDict['user']['displayColor']
        self.createdAt = userDict['user']['createdAt']
        self.previousNames = userDict['user']['previousNames']
        if 'nameChangedAt' in userDict['user']:
            self.nameChangedAt = userDict['user']['nameChangedAt']
            pass
        pass
    pass

# Integration - Return a list of currently connected clients
class Clients():

    __status_code = None
    __response = None

    list = []

    def __init__(self):
        self.__status_code, self.__response = api.postWithAccessToken('/integrations/clients', None)
        if self.__status_code == 200 and not len(self.__response) == 0:
            for userDict in self.__response:
                user = User(userDict)
                self.list.append(user)
                pass
            pass
        pass
    pass

class Chat():

    user = None
    message = None
    chatid = None
    visible = None
    timestamp = None

    def __init__(self, chatDict):
        self.user = User(chatDict['user'])
        self.message = chatDict['body']
        self.chatid = chatDict['id']
        self.visible = chatDict['visible']
        self.timestamp = chatDict['timestamp']
        pass
    pass

# Integrations - Historical Chat Messages
class Chats():

    __status_code = None
    __response = None

    list = []

    def __init__(self):
        self.__status_code, self.__response = api.postWithAccessToken('/integrations/chat', None)
        if self.__status_code == 200:
            for chatDict in self.__response:
                chat = Chat(chatDict)
                self.list.append(chat)
                pass
            pass
        pass
    pass
