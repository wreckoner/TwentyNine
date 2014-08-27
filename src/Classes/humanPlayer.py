'''
Created on Jun 11, 2014
@author: Dibyendu
'''
from display_engine import bidding_module, select_card_module

class HumanPlayerClass():
    '''
    This is a Human player class. Takes a list of cards as parameter
    '''
    def __init__(self, parent, index):
        self.hand = []
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
    
    def choose_card(self, turn_cards):
        '''Calls the select card function of select_a_card module. 
        turn_cards is not really needed. Used to resemble the function signature of computerPlayer class'''
        index = select_card_module.select_a_card(self, self.parent.images['background'])
        return self.hand.pop(index)
        
    def sort_hand(self):
        self.hand = sorted(self.hand, key = lambda x : (x.sort_key, x.priority ))