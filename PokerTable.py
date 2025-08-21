from Players import *
from Card import *
from Chat import distributeChat, chatShowCards, chatTurnChange
import random
from colorama import Fore

CONSTRUCTORS = {Players.GROK:Grok,Players.HUMAN:Human,Players.DEEPSEEK:DeepSeek,Players.ChatGPT:ChatGPT}
BIG_BLIND = 10
SMALL_BLIND = 5
class PokerTable:
    currentTurnPlayer = 0
    currentDealerPlayer = 0
    players = []
    riverCards = []
    deck = []
    turn = 0
    dealer = 0
    pot = 0
    lastToCall = -1

    def __init__ (self,playerIDs):
        # Initialize Deck
        for i in range(4):
            for j in range(13):
                # The deck is a tuple of whether the card has been dealt and what the card is.
                self.deck.append(Card(i,j))
        # Initialize Players
        for num in playerIDs:
            self.players.append(CONSTRUCTORS[num]())
        self.dealCards()
        self.dealer = random.choice(range(len(self.players)))
        self.currentDealerPlayer = self.players[self.dealer]

    def dealCards(self):

        # Shuffle the deck
        random.shuffle(self.deck)

        # Deal two cards to each player sequentially
        for (seatPos,player) in enumerate(self.players):
            player.hand[0] = self.deck[seatPos*2]
            player.hand[1] = self.deck[seatPos*2+1]
            print(f"Player {self.players[seatPos].name}:")
            print(player.stringHand())

        # Set aside the river cards
        self.riverCards = self.deck[len(self.players)*2:len(self.players)*2+5]
        print("River: ")
        for card in self.riverCards: print(card.stringName())
        for player in self.players: print(player.stack)

    
    # Play a single round of Texas Hold'em
    def playRound(self):
        # Begin action at the dealer
        self.lastToCall = self.dealer
        self.turn = self.dealer
        self.currentTurnPlayer = self.players[self.turn]
        distributeChat(Fore.WHITE + f'[PUBLIC:] {self.currentTurnPlayer.name} distributes cards to each player and sets 5 aside for the river',self.players)
        # Increment the dealer
        self.advanceDealer()
        # Advance to the big blind player and charge them the big blind fee
        self.advanceTurn()
        self.chargePlayer(self.currentTurnPlayer, BIG_BLIND)
        distributeChat(Fore.WHITE + f'[PUBLIC:] {self.currentTurnPlayer.name} pitches in the big blind of ${BIG_BLIND} and now has ${self.currentTurnPlayer.stack}',self.players)
        # Advance to the small blind player and charge them the small blind fee
        self.advanceTurn()
        self.chargePlayer(self.currentTurnPlayer, SMALL_BLIND)
        distributeChat(Fore.WHITE + f'[PUBLIC:] {self.currentTurnPlayer.name} pitches in the small blind of ${SMALL_BLIND} and now has ${self.currentTurnPlayer.stack}',self.players)
        # Show all players their hand
        chatShowCards(self.players)

        # Mark UTG player
        self.advanceTurn()
        chatTurnChange(self.players,self.turn)
        self.lastToCall = self.turn
        # I NEED A DO WHILE LOOP!!!!!
        do = True
        # Commence betting cycle
        while(self.turn!=self.lastToCall or do ==True):
            if(do == True): do = False
            else: chatTurnChange(self.players,self.turn)
            self.currentTurnPlayer.getResponse()
            self.advanceTurn()
    
    # Wraparound logic for dealer
    def advanceDealer(self):
        self.dealer+=1
        if self.dealer >= len(self.players):
            self.dealer = 0
        self.currentDealerPlayer = self.players[self.dealer]
    # Wraparound logic for turns
    def advanceTurn(self):
        self.turn+=1
        if self.turn >= len(self.players):
            self.turn = 0
        self.currentTurnPlayer = self.players[self.turn]
    def chargePlayer(self,player: Player, amount: int):
        player.stack-=amount
        self.pot+=amount
        
