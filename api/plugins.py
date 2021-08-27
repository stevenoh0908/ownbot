# plugins.py
# ownbot command 확장에 이용되는 여러 편의기능의 구현 및 기본 확장 뼈대 제공

class ownbotChatCommand():

    chatEvent = None
    arg = None

    def __init__(self, chatEvent):
        self.chatEvent = chatEvent
        self.arg = chatEvent.message[len(chatEvent.message.strip().split()[0])+1:]
        pass
