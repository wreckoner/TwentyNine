'''
Created on Jun 11, 2014
@author: Dibyendu
'''
from display_engine.image_files import card_files

class Card():
    '''
    This is the class of a single card.
    '''
    def __init__(self, suit, character, value, priority, sort_key):
        self.suit = suit
        self.character = character
        self.value = value
        self.priority = priority
        self.sort_key = sort_key
        self.image_file = card_files()[str(self)]
        
    def __repr__(self):
        return "%s - %s" %(self.suit, self.character)

        