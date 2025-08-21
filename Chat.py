from Player import Player
from colorama import Fore
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
    response = input(Fore.GREEN + f'[ACTION:] Type C to call, R to raise, or F to fold: '+Fore.WHITE)
    