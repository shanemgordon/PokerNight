import atexit
from colorama import Fore
from PokerTable import PokerTable
from Players import Players

def resetColor():
    print(Fore.WHITE)

print(__name__)
atexit.register(resetColor)
poker = PokerTable([Players.GROK,Players.ChatGPT,Players.DEEPSEEK,Players.HUMAN])
poker.playRound()

