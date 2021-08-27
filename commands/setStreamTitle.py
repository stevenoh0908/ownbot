# setStreamTitle.py
# ownbot 방제변경

import api.plugins
import api.integrations as bot

class SetStreamTitle(api.plugins.ownbotChatCommand):
    def setStreamTitle(self, title):
        bot.setStreamtitle(title)
        pass
    def __init__(self, chat):
        super().__init__(chat)
        self.setStreamTitle(self.arg)
        pass
    pass

def __init__(chat):
    SetStreamTitle(chat)
    pass