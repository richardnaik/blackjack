from blackjack import BlackJack
from sys import argv

script, bet = argv

blackjack = BlackJack(bet)
BlackJack.play(blackjack)
