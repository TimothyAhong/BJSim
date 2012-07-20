from BJ import *

p = Player("Joe")

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


p.setStrategyByCount('N', basic)
p.setStrategyByCount('L', basic)
p.setStrategyByCount('M', basic)
p.setStrategyByCount('H', basic)
p.setStrategyByCount('VH', basic)

game = BlackjackGame(2, 1.5, 0.75, [p])

outcomes = []
episodes = 2


for k in range(0, episodes):
    print "Shuffle time..."
    game.dealer.shuffleDeck()
    while (not game.requiresShuffle()):
        game.playRound(True)
    outcomes.append(p.getBankroll())
    print str(p.getBankroll())
    #p.setBankroll(0)
    #if k % 10 == 0 and k > 0:  
        #print "Episode " + str(k)

print "Final bankroll: " + str(sum(outcomes))
 
