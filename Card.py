VALUENAMES = ['ACE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING']
SUITNAMES = ['SPADES','HEARTS','DIAMONDS','CLUBS']
class Card:

    suit = 0
    value = 0
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def stringName(self):
        return VALUENAMES[self.value] + ' OF ' + SUITNAMES[self.suit]
    def getSuit(self):
        return SUITNAMES[self.suit]
    def getName(self):
        return VALUENAMES[self.value]