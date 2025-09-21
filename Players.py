from enum import Enum, auto
from Player import Player
from Chat import *
class Players(Enum):
    GROK = 0
    ChatGPT = 1
    DEEPSEEK = 2
    HUMAN = 3
class Moves(Enum):
    RAISE = 'r'
    CALL = 'c'
    FOLD = 'f'

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
        # response = (move, amount (for raising))
        response = (' ', 0)
        response[0] = chatHumanMovePrompt(self)
        if response[0] == Moves.RAISE:
            response[1] = chatHumanRaisePrompt(self)
            
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