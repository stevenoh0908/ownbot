# autoGreetings.py
# ownbot 자동인사 기능

# Make sure all import must be based on cwd: ownbot.
import api.plugins
import api.integrations as bot

class AutoGreetings(api.plugins.ownbotChatCommand):
    def sendGreetings(self, chat):
        bot.sendChat(chat.user.displayName + '님 하이~! 👋')
        pass
    def __init__(self, chat):
        super().__init__(chat)
        self.sendGreetings(chat)
        pass

# Make sure you has __init__ func in your command script! this is called first, when your command is called.
def __init__(chat):
    AutoGreetings(chat)
    pass