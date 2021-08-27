# admin.py
# Admin Api 관리

import api.owncast_api as api

# Admin - Server status and broadcaster
class Status():
    
    __status_code = None
    __response = None

    remoteAddr = None
    time = None
    streamWidth = None
    streamHeight = None
    streamFramerate = None
    streamVideoBitrate = None
    streamVideoCodec = None
    streamAudioBitrate = None
    streamAudioCodec = None
    streamEncoder = None
    online = None
    viewerCount = None
    overallPeakViewerCount = None
    sessionPeakViewerCount = None
    version = None
    
    def __init__(self):
        self.__status_code, self.__response = api.postWithAuth('/admin/status', None)
        if self.__status_code == 200:
            self.remoteAddr = self.__response['broadcaster']['remoteAddr']
            self.time = self.__response['broadcaster']['time']
            self.streamWidth = self.__response['broadcaster']['streamDetails']['width']
            self.streamHeight = self.__response['broadcaster']['streamDetails']['height']
            self.streamFramerate = self.__response['broadcaster']['streamDetails']['framerate']
            self.streamVideoBitrate = self.__response['broadcaster']['streamDetails']['videoBitrate']
            self.streamVideoCodec = self.__response['broadcaster']['streamDetails']['videoCodec']
            self.streamAudioBitrate = self.__response['broadcaster']['streamDetails']['audioBitrate']
            self.streamAudioCodec = self.__response['broadcaster']['streamDetails']['audioCodec']
            self.streamEncoder = self.__response['broadcaster']['streamDetails']['encoder']
            self.online = self.__response['online']
            self.viewerCount = self.__response['viewerCount']
            self.overallPeakViewerCount = self.__response['overallPeakViewerCount']
            self.sessionPeakViewerCount = self.__response['sessionPeakViewerCount']
            self.version = self.__response['versionNumber']
            pass
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

# Admin - Return a list of currently connected clients
class Clients():

    __status_code = None
    __response = None

    list = []

    def __init__(self):
        self.__status_code, self.__response = api.postWithAuth('/admin/chat/clients', None)
        if self.__status_code == 200 and not len(self.__response) == 0:
            for userDict in self.__response:
                user = User(userDict)
                self.list.append(user)
                pass
            pass
        pass
    pass

class Log():

    message = None
    level = None
    timestamp = None

    def __init__(self, logDict):
        self.message = logDict['message']
        self.level = logDict['level']
        self.time = logDict['time']
        pass
    pass

# Admin - Return recent log entries
class Logs():

    __status_code = None
    __response = None

    list = []

    def __init__(self):
        self.__status_code, self.__response = api.postWithAuth('/admin/logs', None)
        if self.__status_code == 200:
            for logDict in self.__response:
                log = Log(logDict)
                self.list.append(log)
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

# Admin - Chat messages, unfiltered
class Chats():

    __status_code = None
    __response = None

    list = []

    def __init__(self):
        self.__status_code, self.__response = api.postWithAuth('/admin/chat/messages', None)
        if self.__status_code == 200:
            for chatDict in self.__response:
                chat = Chat(chatDict)
                self.list.append(chat)
                pass
            pass
        pass
    pass

class TimestampedValue():

    time = None
    count = None

    def __init__(self, timestampedvalueDict):
        self.time = timestampedvalueDict['time']
        self.count = timestampedvalueDict['value']
        pass
    pass

# Admin - Viewers Over Time
class ViewerCounts():

    __status_code = None
    __response = None

    list = []

    def __init__(self):
        self.__status_code, self.__response = api.postWithAuth('/admin/viewersOverTime', None)
        if self.__status_code == 200:
            for viewercountDict in self.__response:
                viewercount = TimestampedValue(viewercountDict)
                self.list.append(viewercount)
                pass
            pass
        pass
    pass

# Admin - Hardware Stats
class HardwareStats():
    
    __status_code = None
    __response = None

    cpu = []
    memory = []
    disk = []

    def __init__(self):
        self.__status_code, self.__response = api.postWithAuth('/admin/hardwarestats', None)
        if self.__status_code == 200:
            cpuDicts = self.__response['cpu']
            memoryDicts = self.__response['memory']
            diskDicts = self.__response['disk']
            for cpuDict in cpuDicts:
                c = TimestampedValue(cpuDict)
                self.cpu.append(c)
                pass
            for memoryDict in memoryDicts:
                m = TimestampedValue(memoryDict)
                self.memory.append(m)
                pass
            for diskDict in diskDicts:
                d = TimestampedValue(diskDict)
                self.disk.append(d)
                pass
            pass
        pass
    pass

# Admin - Update the visiblity of chat messages
def updateMessageVisibility(chatids, visible):
    __status_code, __response = api.postWithAuth('/admin/chat/updatemessagevisibility',
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

# Admin - Enable or disable a single user
def setUserEnabled(userid, enabled):
    __status_code, __response = api.postWithAuth('/admin/chat/users/setenabled',
    {
        'userId': userid,
        'enabled': enabled
    })
    if __status_code == 200:
        return __response['success']
        pass
    else:
        return False
        pass
    pass

# Admin - Set the stream title
def setStreamTitle(title):
    __status_code, __response = api.postWithAuth('/admin/config/streamtitle',
     {
        "value": title
     })
    if __status_code == 200:
        return __response['success']
        pass
    else:
        return False
        pass
    pass

# Admin - Mark if your stream is not safe for work
def setNSFW(enabled):
    __status_code, __response = api.postWithAuth('/admin/config/nsfw', {
        'value': enabled
    })
    if __status_code == 200:
        return __response['success']
        pass
    else:
        return False
        pass
    pass
