from abc import ABC, abstractmethod
from Card import Card
from colorama import Fore
DEFAULT_STACK = 100
class Player(ABC):
    name = ""
    stack = DEFAULT_STACK
    seat = 0
    hand = [Card(0,0),Card(0,0)]
    chatLog = []
    color = Fore.WHITE
    #@abstractmethod
    def __init__(self):
        self.stack = DEFAULT_STACK
    # Should return an ActionCode and associated text
    def getResponse(self):
        pass
    
    #@abstractmethod
    # Add a message to the player's context log. 
    def addMessage(self,text:str):
        pass

    def stringHand(self):
        return "1: " + self.hand[0].stringName() + " 2: " + self.hand[1].stringName()