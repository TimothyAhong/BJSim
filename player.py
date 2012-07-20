from dealer import *

class Player(Human):
    def __init__(self, name="Player"):
        Human.__init__(self)
        self.name = name
        self.bankroll = 0
        self.strategybycount = {} #mapping count to strategy dictionary
        self.iscounter = False
        self.count = 0
        self.statistics = {}
        self.resetStatistics()
    
    def resetStatistics(self):
        self.statistics["TotalWins"] = 0
        self.statistics["TotalLosses"] = 0
        self.statistics["TotalPushes"] = 0
        self.statistics["Blackjacks"] = 0
        self.statistics["Wins-Faceup:A"] = {}
        for v in range(2, 11):
            self.statistics["Wins-Faceup:" + str(v)] = {}
        self.statistics["Losses-Faceup:A"] = {}
        for v in range(2, 11):
            self.statistics["Losses-Faceup:" + str(v)] = {}
        self.statistics["Pushes-Faceup:A"] = {}
        for v in range(2, 11):
            self.statistics["Pushes-Faceup:" + str(v)] = {}
    
    def getStatistics(self):
        return self.statistics
    
    def logRound(self, dealerhand, playerhand, winner):
        faceup = dealerhand.getCard(0)[0]
        if faceup in ['K', 'Q', 'J', 'T']:
            faceup = '10'
        if winner > 0:
            if winner == 2:
                self.statistics["Blackjacks"] = self.statistics["Blackjacks"] + 1
            self.statistics["TotalWins"] = self.statistics["TotalWins"] + 1
            try:
                self.statistics["Wins-Faceup:" + faceup][self.getHandID(Hand(playerhand.toList()[0:2]))] = self.statistics["Wins-Faceup:" + faceup][self.getHandID(Hand(playerhand.toList()[0:2]))] + 1
            except:
                self.statistics["Wins-Faceup:" + faceup][self.getHandID(Hand(playerhand.toList()[0:2]))] = 1
        elif winner == 0:
            self.statistics["TotalPushes"] = self.statistics["TotalPushes"] + 1
            try:
                self.statistics["Pushes-Faceup:" + faceup][self.getHandID(playerhand.toList()[0:2])] = self.statistics["Pushes-Faceup:" + faceup][self.getHandID(Hand(playerhand.toList()[0:2]))] + 1
            except:
                self.statistics["Pushes-Faceup:" + faceup][self.getHandID(Hand(playerhand.toList()[0:2]))] = 1 
        else:
            self.statistics["TotalLosses"] = self.statistics["TotalLosses"] + 1
            try:
                self.statistics["Losses-Faceup:" + faceup][self.getHandID(Hand(playerhand.toList()[0:2]))] = self.statistics["Losses-Faceup:" + faceup][self.getHandID(Hand(playerhand.toList()[0:2]))] + 1
            except:
                self.statistics["Losses-Faceup:" + faceup][self.getHandID(Hand(playerhand.toList()[0:2]))] = 1
    
    def resetCount(self):
        self.count = 0
    
    #change so that on init every human is given an array
    #the form is card=>count value
    def countCard(self, card): #basic hi-lo count
        if card[0] in ['A', 'K', 'Q', 'J', 'T']:
            self.count = self.count - 1
        elif card[0] in ['2', '3', '4', '5', '6']:
            self.count = self.count + 1
    
    def getBankroll(self):
        return self.bankroll
    
    def setBankroll(self, br):
        self.bankroll = br
    
    def adjustBankroll(self, amount):
        self.bankroll = self.bankroll + amount
    
    def getHandID(self, hand):
        handid = ''
        if len(hand) == 2:
            if self.canSplit(hand):
                handid = 'P'
                handid = handid + str(self.evaluateCard(hand.getCard(0)))
                return handid
            elif hand.getCard(0)[0] == 'A':
                handid = 'A'
                handid = handid + str(self.evaluateCard(hand.getCard(1)))
                return handid
            elif hand.getCard(1)[0] == 'A':
                handid = 'A'
                handid = handid + str(self.evaluateCard(hand.getCard(0)))
                return handid
        if self.evaluateHand(hand) > 16:
            return str(self.evaluateHand(hand))
        else:
            return str(self.softValue(hand))
    
    #change this to call the play specific function
    def makeWager(self): #modify this 
        if self.count >= 10 and self.count < 15:
            return 50
        elif self.count >= 15:
            return 100
        else:
            return 10
    
    #not actually count based but based on on the return of CountID
    def setStrategyByCount(self, count, strategy):
        self.strategybycount[count] = strategy
    
    def takeInsurance(self): #modify this
        return False
    
    #change to call player specefic function
    def getCountID(self, count): #modify this
        if count <= 0:
            return 'N' #negative/neutral
        elif count in [1, 2]:
            return 'L' #low
        elif count in [3, 4, 5]:
            return 'M' #medium
        elif count in [6, 7, 8]:
            return 'H' #high
        else:
            return 'VH' #very high     
    
    def makeDecision(self, upcard, index=1, verbose=True, candouble=True, cansplit=True): #makes a decision about the hand labeled "index" given the count
        try:
            strategy = self.strategybycount[self.getCountID(self.count)]
            policy = strategy[self.getHandID(self.currenthands[index - 1])]
            deckval = range(2, 11)
            try:
                i = deckval.index(self.evaluateCard(upcard)) 
            except:
                i = 9
            move = policy[i]
            if verbose:
                if move == 'H':
                    print self.name + " hits"
                elif move == 'D':
                    print self.name + " doubles down"
                elif move == 'P':
                    print self.name + " splits"
                elif move == 'S':
                    print self.name + " stays"
            if move == 'D' and not candouble:
                move = 'H'
            elif move == 'P' and not cansplit:
                hand = self.currenthands[index - 1]
                sum = self.evaluateHand(hand)
                policy = strategy[str(sum)]
                try:
                    i = deckval.index(self.evaluateCard(upcard))
                except:
                    i = 9
                move = policy[i]
            return move
        except:
            return 'S'
        
