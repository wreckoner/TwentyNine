'''
Created on Jun 11, 2014
@author: Dibyendu
'''
from game_play import decisionLogic
import random


class ComputerPlayerClass():
    '''
    This is a computer player class. Takes a hand of cards as parameter.
    '''
    def __init__(self, hand, index, parent):
        self.hand = hand
        self.parent = parent
        self.trump = False
        self.index = index
        self.loc = []
        
    def __repr__(self):
        return "CPU %s" %self.index
    
    def MakeBid(self):
        choices = range(16,24) + [False for _ in range(1,8)]
        while True:
            bid = random.choice(choices)
            if len(self.parent.bids) != 0 and bid and bid <= max(self.parent.bids): bid = random.choice([False, bid + 1])
            else: break
        print "%s bid : %s" %(self, bid if bid is not False else "pass")
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
            self.parent.trump = max(temp)[0]
            
    def choose_card(self, turn_cards):
        # Chooses a card from its hand.
        choice = decisionLogic.random_card_select(self, turn_cards)
        print "%s played %s" %(self.__repr__(), choice)
        return choice
        
    def sort_hand(self):
        self.hand = sorted(self.hand, key = lambda x : (x.sort_key, x.priority ))