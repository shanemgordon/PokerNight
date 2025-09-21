from Player import Player
from Players import Moves
from colorama import Fore
from PokerTable import PokerTable
def distributeChat(message:str, players: list, target = -1):
    for n,player in enumerate(players):
        player.addMessage(message)
def chatShowCards(players: list):
    for player in players:
        player.addMessage(Fore.WHITE + f'[PUBLIC:] Your cards are as follows: {player.stringHand()}')
def chatTurnChange(players: list,turn: int):
    for n,player in enumerate(players):
        if n == turn:
            player.addMessage(Fore.GREEN + f'[ACTION:] It is now your turn')
        else:
            player.addMessage(Fore.WHITE + f'[PUBLIC:] It is now {players[turn].name}\'s turn')
    
def chatHumanMovePrompt(player: Player):
    move = ' '
    while move not in Moves:
        move = input(Fore.GREEN + f'[ACTION:] Type C to call, R to raise, or F to fold: '+Fore.WHITE).lower()
    return move
def chatHumanRaisePrompt(player: Player, table: PokerTable):
    amount = table.bet
    while(True):
        amount = input(Fore.GREEN + f'[ACTION:] The current table bet is {amount}. What would you like to raise it to?')
        if(amount < table.bet):
            print(Fore.RED + f'[ERROR:] That amount is less than the current table bet')