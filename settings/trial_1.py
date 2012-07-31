###
# Settings for a trial
# To begin trial simply run this script with argv[1] = thread number
# ID: 1
# Name: 
# Player ids: 1
# Game ids: 1
# Description:  Verbose short trial to test functionality
#               Single Hi-Lo counter and the dealer
#               4 deck shoe 
#               100 shoes
#
###

#==========================================================
#Import deps (DO NOT CHANGE)
#==========================================================
import sys
sys.path.append("../bjsim")
sys.path.append("../settings")
sys.path.append("../settings/player")
sys.path.append("../settings/game")
sys.path.append("../settings/trial")
from BJ import *
from trial import *

#==========================================================
#Setup export thread number (DO NOT CHANGE)
#==========================================================
if len(sys.argv)>1:
    thread_number = sys.argv[1]
else:
    thread_number = 1

#==========================================================
#Import trial specefic settings (EDITABLE)
#==========================================================
from player_1 import *
from game_1 import *

#==========================================================
#Add players and game to trial(EDITABLE)
#==========================================================
num_shoes = 100
game_1.players = [player_1]
trial = Trial(game_1,num_shoes)

#==========================================================
#Other trial settings(EDITABLE)
#==========================================================
trial.id = 1
trial.verbose = True
trial.enable_hand_log = False
trial.enable_trial_log = True
trial.enable_shoe_log =True

#==========================================================
#Setup export settings(not yet implemented) (EDITABLE)
#==========================================================


#==========================================================
#Run the trial (DO NOT CHANGE)
#==========================================================
trial.run(thread_number)
