# server.py
# Server API 관리

import api.owncast_api as api

class SocialHandle():

    platform = None
    url = None

    def __init__(self, socialhandleDict):
        self.platform = socialhandleDict['platform']
        self.url = socialhandleDict['url']
        pass
    pass

class Info():

    __status_code = None
    __response = None

    name = None
    summary = None
    logo = None
    tags = []
    socialHandles = []
    extraPageContent = None
    version = None
    nsfw = None
    streamTitle = None
    chatDisabled = None

    def __init__(self):
        self.__status_code, self.__response = api.get('/config')
        if self.__status_code == 200:
            self.name = self.__response['name']
            self.summary = self.__response['summary']
            self.logo = self.__response['logo']
            self.tags = self.__response['tags']
            self.nsfw = self.__response['nsfw']
            self.streamTitle = self.__response['streamTitle']
            for socialhandleDict in self.__response['socialHandles']:
                socialHandle = SocialHandle(socialhandleDict)
                self.socialHandles.append(socialHandle)
                pass
            self.extraPageContent = self.__response['extraPageContent']
            self.version = self.__response['version']
            self.chatDisabled = self.__response['chatDisabled']
            pass
        pass
    pass

class Status():

    __status_code = None
    __response = None

    lastConnectTime = None
    lastDisconnectTime = None
    online = None
    versionNumber = None
    streamTitle = None
    viewerCount = None

    def __init__(self):
        self.__status_code, self.__response = api.get('/status')
        if self.__status_code == 200:
            self.lastConnectTime = self.__response['lastConnectTime']
            self.lastDisconnectTime = self.__response['lastDisconnectTime']
            self.online = self.__response['online']
            self.versionNumber = self.__response['versionNumber']
            self.streamTitle = self.__response['streamTitle']
            self.viewerCount = self.__response['viewerCount']
            pass
        pass
    pass
