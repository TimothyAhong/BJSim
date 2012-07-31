import random

#Save the seed in the deck and output to log file for analysis?
random.seed()

class Deck:
    def __init__(self, num):
        self.numdecks = num
        self.shuffle()
    
    def getNumberDecks(self):
        return self.numdecks
    
    def getNumberCardsLeft(self):
        return len(self.deck)
    
    def drawCard(self):
        if len(self.deck) > 0:
            card = random.choice(self.deck)
            self.deck.remove(card)
            return card    
    
    def shuffle(self):
        #Define all card values
        deckval = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        self.deck = []
        for value in deckval:
            #Append suits
            for copy in range(0, self.numdecks):
                self.deck.append(value + 'H')
                self.deck.append(value + 'D')
                self.deck.append(value + 'S')
                self.deck.append(value + 'C') 
        #Python random shuffler? Look into this
        random.shuffle(self.deck)

class Hand:
    def __init__(self, c):
        self.cards = c
        self.wager = 0
    def setWager(self, w):
        self.wager = w
    def getWager(self):
        return self.wager
    def __str__(self):
        return str(self.cards)
    def append(self, card):
        self.cards.append(card)
    def __len__(self):
        return len(self.cards)
    def getCard(self, index):
        return self.cards[index]
    def toList(self):
        return self.cards


class Human:
    def __init__(self):
        self.name = ""
        self.currenthands = []
    def clearHand(self, index):
        if index - 1 < len(self.currenthands):
            del self.currenthands[index - 1]
    def clearHands(self):
        self.currenthands = [] #clears all hands
    def takeCard(self, card, index=1):
        if index - 1 < len(self.currenthands):
            self.currenthands[index - 1].append(card) #add a card to the hand labeled "index"
        else:
            newhand = Hand([]) #if the index is greater than the current number of hands, create a new hand
            newhand.append(card)
            self.currenthands.append(newhand)
    def getHand(self, index=1): #gets one hand labeled index
        if index - 1 < len(self.currenthands):
            return self.currenthands[index - 1]
    def getHands(self): #gets all hands in a list
        return self.currenthands
    def setName(self, n):
        self.name = n
    def getName(self):
        return self.name
    def hasAce(self, hand):
        for card in hand.toList():
            if card[0] == 'A':
                return True
        return False
    def canSplit(self, hand):
        if len(hand) == 2:
            if self.evaluateCard(hand.getCard(0)) == self.evaluateCard(hand.getCard(1)):
                return True
        return False
    def isBlackjack(self, hand):
        if len(hand) == 2:
            if self.evaluateHand(hand) == 21:
                return True
        return False
    def softValue(self, hand):
        val = 0
        for card in hand.toList():
            val = val + self.evaluateCard(card)
        return val    
    def evaluateHand(self, hand):
        val = self.softValue(hand)
        for card in hand.toList():
            if card[0] == 'A':
                if val + 10 <= 21:
                    val = val + 10         
        return val  
    def evaluateCard(self, fullcard):
        if not fullcard == "NULL":
            card = fullcard[0]
            val = 0
            if card in ['K', 'Q', 'J', 'T']:  
                val = 10
            elif card == 'A':
                val = 1
            else:
                val = int(card)
            return val
        else:
            return 0
        
class Dealer(Human):
    def __init__(self, num, hs17=True):
        Human.__init__(self)
        self.name = "Dealer"
        self.deck = Deck(num)
        self.hitsoft17 = hs17
    
    def getNumberDecks(self):
        return self.deck.getNumberDecks()
    
    def shuffleDeck(self):
        self.deck.shuffle()
    
    def dealCard(self):
        return self.deck.drawCard()

    #Move to table based system
    def mustHit(self):
        currenttotal = self.evaluateHand(self.getHand())
        if currenttotal < 17:
            return True
        elif currenttotal == 17:
            if self.softValue(self.getHand()) < 17:
                return True
            else:
                return False
        else:
            return False
    
    def evaluateWinner(self, dealerhand, playerhand): #returns -1 for dealer, 0 for push, 1 for player, 2 for win by blackjack
        dealerval = self.evaluateHand(dealerhand)
        playerval = self.evaluateHand(playerhand)
        if self.isBlackjack(playerhand) and not self.isBlackjack(dealerhand):
            return 2
        elif self.isBlackjack(dealerhand) and not self.isBlackjack(playerhand):
            return -1
        elif(playerval > 21):
            return -1
        else:
            if(dealerval > 21):
                return 1
            elif(playerval > dealerval):
                return 1
            elif(playerval == dealerval):
                return 0
            else:
                return -1
                
    def getNumberCardsLeft(self):
        return self.deck.getNumberCardsLeft()
        


 
 
 
 