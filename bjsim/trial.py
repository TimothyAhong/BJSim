from export import *
import datetime

class Trial:
    def __init__(self, game, num_shoes):
        self.game = game
        self.num_shoes=num_shoes
        self.verbose=False
        self.enable_trial_log=True
        self.enable_shoe_log=True
        self.enable_hand_log=True
        self.statistics = {}
        self.statistics['decksPlayed'] = 0
        #start time in s
        self.statistics['startTime'] = 0
        self.game_id=game.id

    def getTime(self):
        now = datetime.datetime.now()
        return now.second + 60*(now.minute+60*(now.hour+24*now.day))

    def run(self,thread_num):
        exporter.setup(thread_num)
        exporter.trial_id = self.id
        exporter.open_files()
        self.statistics['startTime'] = self.getTime()

        #init all the players
        for player in self.game.players:
            # WARNING: This slows things down considerably if enabled
            player.enable_hand_log =  self.enable_hand_log
            player.resetStatistics()
            player.game_id=self.game_id
            #is this by reference or value? it should be by reference so that
            #both the trial and player are using the same exporter...
            player.exporter = exporter

        #run through all the shoes
        for i in range(0,self.num_shoes):

            for player in self.game.players:
                player.newShoeStatistics()

            #play through a shoe
            self.game.dealer.shuffleDeck()
            while not self.game.requiresShuffle():
                self.game.playRound(self.verbose)

            #update number of decks played
            self.statistics['decksPlayed'] += self.game.dealer.getNumberDecks() - (self.game.dealer.getNumberCardsLeft()/52)

            #log the shoe
            if self.enable_shoe_log:
                for player in self.game.players:
                    player.logShoe()
                #=log information regarding the most recent shoe

        if self.enable_trial_log:
            #log the trial data
            self.statistics['endTime'] = self.getTime()
            elapsedTime = self.statistics['endTime']-self.statistics['startTime']
            data = [self.statistics['startTime'],elapsedTime,self.statistics['decksPlayed']]
            exporter.t(data)

            #log the player trial information
            for player in self.game.players:
                player.logTrial()
            #=log information regarding this trial
            
        exporter.close_files()
 