###
# Settings for a game
#
# ID: 1
# Name: Eddard Stark
# Rules: 4 decks, 1.5x payoff for blackjacks and 75% deck penetration 
# Who plays by these rules?: 
#
###

#==========================================================
#Import deps
#==========================================================
from BJ import *

#==========================================================
#Game settings
#==========================================================
decks = 6
deck_penetration = 0.75
bj_payoff = 1.5

#==========================================================
#Init game
#==========================================================
game_1 = BlackjackGame(decks, bj_payoff, deck_penetration, [])
game_1.id=1