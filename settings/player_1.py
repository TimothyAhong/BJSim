###
# Settings for a player
#
# ID: 1
# Name: Eddard Stark
# Betting units: 100
# Method: Hi Lo ... (not fully implemented)
# Method Source: (internet source or somethin)
#
###

#==========================================================
#Import deps
#==========================================================
from player import * 

#==========================================================
#Import player specific strategies
#==========================================================
from basic_strategy import *

#==========================================================
#Setup player
#==========================================================
player_1 = Player("Eddard Stark")
player_1.id = 1
player_1.setBankroll(100)

#==========================================================
#Add player strategies
#==========================================================
player_1.setStrategyByCount('N', basic)
player_1.setStrategyByCount('L', basic)
player_1.setStrategyByCount('M', basic)
player_1.setStrategyByCount('H', basic)
player_1.setStrategyByCount('VH', basic)
