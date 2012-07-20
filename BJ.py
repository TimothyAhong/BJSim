from player import *

 
class BlackjackGame:
    def __init__(self, numdecks, blackjack, dp, playerlist):
        self.players = playerlist
        self.deckpen = max(0, 1 - dp)
        self.blackjackpayoff = blackjack
        self.dealer = Dealer(numdecks)
    
    def getPlayerBankrolls(self): #returns a dictionary of player's bankroll
        rolls = {}
        for p in self.players:
            rolls[p] = p.getBankroll()
        return rolls
    
    def revealHandToCount(self, hand):
        for p in self.players:
            for c in hand.toList():
                p.countCard(c)
    
    def offerInsurance(self, verbose):
        for p in self.players:
            insure = p.takeInsurance()
            if insure:
                if verbose:
                    print p.getName() + " takes insurance"
                if self.dealer.isBlackjack(self.dealer.getHand()):
                    p.adjustBankroll(p.getHand().getWager()/2)
                else:
                    p.adjustBankroll(-p.getHand().getWager()/2)
            else:
                if verbose:
                    print p.getName() + " refuses insurance"
    
    def playHand(self, dealerupcard, player, index=1, handnumber=1, verbose=True, candouble=True, cansplit=True):
        if handnumber == 1 and self.dealer.isBlackjack(player.getHand()):
            if verbose:
                print player.getName() + " has blackjack!"
        else:
            decision = player.makeDecision(dealerupcard, index, verbose, candouble, cansplit)
            if decision == 'D': #double down - double wager & take one card
                player.getHand(index).setWager(2*player.getHand(index).getWager())
                player.takeCard(self.dealer.dealCard(), index)
                if verbose:
                    print player.getName() + "'s final hand " + str(index) + ": " + str(player.getHand(index)) + "(" + str(self.dealer.evaluateHand(player.getHand(index))) + ")"
            elif decision == 'P': #split 
                hand = player.getHand(index)
                origwager = hand.getWager()
                card1 = hand.getCard(0)
                card2 = hand.getCard(1)
                player.clearHand(index)
                player.takeCard(card1, index)
                player.takeCard(self.dealer.dealCard(), index)
                player.getHand(index).setWager(origwager)
                self.playHand(dealerupcard, player, index, handnumber + 1, verbose=verbose, candouble=True, cansplit=True)
                player.takeCard(card2, index + 1)
                player.takeCard(self.dealer.dealCard(), index + 1)
                player.getHand(index + 1).setWager(origwager)
                self.playHand(dealerupcard, player, index + 1, handnumber + 1, verbose=verbose, candouble=True, cansplit=True)
            else:
                while decision == 'H' and self.dealer.evaluateHand(player.getHand(index)) < 22:
                    player.takeCard(self.dealer.dealCard(), index)
                    if self.dealer.evaluateHand(player.getHand(index)) > 21:
                        if verbose:
                            print player.getName() + " busts"
                    else:
                        decision = player.makeDecision(dealerupcard, index, verbose, False, False)
                if verbose:
                    print player.getName() + "'s final hand " + str(index) + ": " + str(player.getHand(index)) + "(" + str(self.dealer.evaluateHand(player.getHand(index))) + ")"
    
    def settleRound(self, verbose=True):
        dealerhand = self.dealer.getHand()
        self.revealHandToCount(dealerhand)
        for p in self.players:
            for hand in p.getHands():
                self.revealHandToCount(hand)
                winner = self.dealer.evaluateWinner(dealerhand, hand)
                p.logRound(dealerhand, hand, winner)
                if verbose:
                    if winner > 0: 
                        if winner == 2:
                            print p.getName() + " wins " + str(self.blackjackpayoff*hand.getWager())
                        else:
                            print p.getName() + " wins " + str(hand.getWager())
                    elif winner < 0:
                        print p.getName() + " loses " + str(hand.getWager())
                    else:
                        print p.getName() + " pushes"
                if winner == 2: #win by blackjack
                    p.adjustBankroll(self.blackjackpayoff*hand.getWager())
                else:
                    p.adjustBankroll(winner*hand.getWager())
            p.clearHands()
        self.dealer.clearHands()

    def playRound(self, verbose=True):
        if self.dealer.getNumberCardsLeft() < self.deckpen*52*self.dealer.getNumberDecks():
            if verbose:
                print "Shuffling..."
            self.dealer.shuffleDeck()
            for p in self.players:
                p.resetCount()
        wagers = {} #map player to their wager
        for p in self.players:
            wager = p.makeWager()
            if verbose:
                print p.getName() + "'s wager: " + str(wager)
            p.takeCard(self.dealer.dealCard())
            p.takeCard(self.dealer.dealCard())
            p.getHand().setWager(wager)
            if verbose:
                print p.getName() + "'s hand: " + str(p.getHand())
        dealerupcard = self.dealer.dealCard()
        if verbose:
            print "Dealer's upcard: " + str(dealerupcard)
        self.dealer.takeCard(dealerupcard)
        self.dealer.takeCard(self.dealer.dealCard())
        if dealerupcard[0] == 'A':
            if verbose:
                print "Ace showing...insurance?"
            self.offerInsurance(verbose=verbose)
        if self.dealer.isBlackjack(self.dealer.getHand()):
            if verbose:
                print "Dealer has blackjack"
            self.settleRound(verbose=verbose)
        else:
            if verbose:
                print "Dealer does not have blackjack"
            for p in self.players:
                self.playHand(dealerupcard, p, verbose=verbose)
            while self.dealer.mustHit():
                if verbose:
                    print "Dealer hits"
                self.dealer.takeCard(self.dealer.dealCard())
            if verbose:
                print "Dealer's final hand: " + str(self.dealer.getHand()) + "(" + str(self.dealer.evaluateHand(self.dealer.getHand())) + ")"
            self.settleRound(verbose=verbose)


basic = {}

basic['P2'] = ['P', 'P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H']
basic['P3'] = ['P', 'P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H']
basic['P4'] = ['H', 'H', 'H', 'P', 'P', 'H', 'H', 'H', 'H', 'H']
basic['P5'] = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H']
basic['P6'] = ['P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H', 'H'] 
basic['P7'] = ['P', 'P', 'P', 'P', 'P', 'P', 'H', 'H', 'H', 'H'] 
basic['P8'] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
basic['P9'] = ['P', 'P', 'P', 'P', 'P', 'S', 'P', 'P', 'S', 'S'] 
basic['P10'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']   
basic['P1'] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']  
basic['A2'] = ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H']
basic['A3'] = ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H']   
basic['A4'] = ['H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H']
basic['A5'] = ['H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H']
basic['A6'] = ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H']
basic['A7'] = ['S', 'D', 'D', 'D', 'D', 'S', 'S', 'H', 'H', 'H']
basic['A8'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'] 
basic['A9'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'] 
basic['A10'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
basic['3'] = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'] 
basic['4'] = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']  
basic['5'] = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'] 
basic['6'] = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
basic['7'] = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']  
basic['8'] = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'] 
basic['9'] = ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'] 
basic['10'] = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'] 
basic['11'] = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H'] 
basic['12'] = ['H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H']
basic['13'] = ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H']  
basic['14'] = ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H']
basic['15'] = ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H']
basic['16'] = ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H']
basic['17'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
basic['18'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
basic['19'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
basic['20'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
basic['21'] = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
           


 





 