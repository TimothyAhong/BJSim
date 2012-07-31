###
# RUNNING
# $python sample.py "thread_number"
# Runs the trial as specified below
# Run this script with argument 1 being the thread number
# Conflicting thread numbers will result in file collisions
#
# CONFIGURATION
# Edit the configuration.py file
# Lists/includes the players, dealer and trial
#
###

#==========================================================
#Import deps
#==========================================================
import sys
import os
sys.path.append(os.getcwd()+"/bjsim")
sys.path.append(os.getcwd()+"/settings")
sys.path.append(os.getcwd()+"/settings/player")
sys.path.append(os.getcwd()+"/settings/dealer")
from BJ import *
from trial import *
from export import *

from player_1 import *

game = BlackjackGame(2, 1.5, 0.75, [player_1])

outcomes = []
episodes = 2


for k in range(0, episodes):
    print "Shuffle time..."
    game.dealer.shuffleDeck()
    while (not game.requiresShuffle()):
        game.playRound(True)
    outcomes.append(player_1.getBankroll())
    print str(player_1.getBankroll())
    #p.setBankroll(0)
    #if k % 10 == 0 and k > 0:  
        #print "Episode " + str(k)

print "Final bankroll: " + str(sum(outcomes))
