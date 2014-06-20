'''
Created on Jun 11, 2014
@author: Dibyendu
'''
from GamePlay import decisionLogic
import random

class ComputerPlayerClass():
    '''
    This is a computer player class. Takes a hand of cards as parameter.
    '''
    def __init__(self, hand, index):
        self.hand = sorted(hand,key = lambda x : x.suit)
        self.trump = False
        self.index = index
        
    def __repr__(self):
        return "CPU. ID - %s" %self.index
    
    def MakeBid(self):
        # Makes a bid or passes to the next player
        choices = range(16, 23)
        for _ in range(0, 10):
            choices.append(False)
        return random.choice(choices)
    
    def SelectTrump(self):
        temp = [["diamonds", 0], ["spades", 0], ["hearts", 0], ["clubs", 0]]
        for card in self.hand:
            if card.suit is temp[0][0]:
                temp[0][1] += 1
            elif card.suit is temp[1][0]:
                temp[1][1] += 1
            elif card.suit is temp[2][0]:
                temp[2][1] += 1
            else:
                temp[3][1] += 1
            self.trump = max(temp)[0]
            return self.trump
            
        
    def ChooseCard(self, table):
        # Chooses a card from its hand. Takes a table as parameter.
        (self.hand, table) = decisionLogic.RandomCardSelect(self.hand, table)
        print "%s played %s" %(self.__repr__(), table[-1])
        return table