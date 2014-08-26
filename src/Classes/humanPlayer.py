'''
Created on Jun 11, 2014
@author: Dibyendu
'''
from display_engine import bidding_module

class HumanPlayerClass():
    '''
    This is a Human player class. Takes a list of cards as parameter
    '''
    def __init__(self, hand, index, parent):
        self.hand = hand
        self.parent = parent
        self.index = index
        self.trump = False
        self.loc = []
        self.clicked = 8        # Used to keep track of which card has been selected
        self.selected_card_index = 8
    
    def __repr__(self):
        return "Human %s" %self.index
    
    def make_bid(self, max_bid):
        return bidding_module.user_bidding(self, max_bid)
    
    def select_trump(self):
        self.trump = bidding_module.select_trump_by_user(self)
        return self.trump
    
    def choose_card(self):
        # redundant method in graphic game, since card selection is done graphically.
        choice = self.hand[self.selected_card_index]
        self.parent.played_turn.append(choice)
        self.hand.remove(choice)
        print 'you played', choice
        self.selected_card_index, self.clicked = 8, 8
        
    def sort_hand(self):
        self.hand = sorted(self.hand, key = lambda x : (x.sort_key, x.priority ))