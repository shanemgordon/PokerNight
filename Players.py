from enum import Enum, auto
from Player import Player
from Chat import *
class Players(Enum):
    GROK = 0
    ChatGPT = 1
    DEEPSEEK = 2
    HUMAN = 3

class Grok(Player):
    def __init__(self):
        super()
        self.name = 'Grok'
    def getResponse(self):
        pass
    key = 1
class Human(Player):
    def __init__(self):
        super()
        self.name = 'Human'
    def getResponse(self):
        chatHumanMovePrompt(self)

    def addMessage(self,text:str):
        print(text)

class DeepSeek(Player):
    def __init__(self):
        super()
        self.name = 'DeepSeek'
    def getResponse(self):
        pass
    key = 3
class ChatGPT(Player):
    def __init__(self):
        super()
        self.name = 'ChatGPT'
    def getResponse(self):
        pass
    key = 4