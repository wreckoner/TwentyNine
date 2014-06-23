'''
Created on Jun 11, 2014
@author: Dibyendu
'''
from GamePlay import decisionLogic
import random
from Display import PrintToConsole


class ComputerPlayerClass():
    '''
    This is a computer player class. Takes a hand of cards as parameter.
    '''
    def __init__(self, hand, index, parent):
        self.hand = sorted(hand,key = lambda x : x.suit)
        self.parent = parent
        self.trump = False
        self.index = index
        
    def __repr__(self):
        return "CPU. ID - %s" %self.index
    
    def MakeBid(self):
        choices = range(16,24)
        for _ in range(1,10): choices.append(False)
        while True:
            bid = random.choice(choices)
            if bid in self.parent.bids: bid = random.choice(choices)
            else: break
        PrintToConsole.print_to_console(("%s bid : %s" %(self, bid if bid is not False else "pass")))
        return bid
    
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
            
    def ChooseCard(self, turn_cards):
        # Chooses a card from its hand. Takes a turn_cards as parameter.
        (self.hand, turn_cards) = decisionLogic.RandomCardSelect(self.hand, turn_cards)
        PrintToConsole.print_to_console(("%s played %s" %(self.__repr__(), turn_cards[-1])))
        #return turn_cards