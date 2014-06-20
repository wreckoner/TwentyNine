'''
Created on Jun 11, 2014

@author: Dibyendu
'''

class Card():
    '''
    This is the class of a single card.
    '''
    def __init__(self, suit, character, value, priority):
        self.suit = suit
        self.character = character
        self.value = value
        self.priority = priority
        
    def __repr__(self):
        return "%s - %s" %(self.suit, self.character)