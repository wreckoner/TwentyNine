'''
@author : Dibyendu Das
This module contains the decision logics of the computer players
'''
import random

    
def random_card_select(player, turn_cards):
    ''' A simple card selection algorithm for the AI
    If a suit card is present plays a random, else plays a random of any suit.'''
    if len(turn_cards) == 0:            # if first player, selects a random card
        print 'first player'
        choice = random.choice(player.hand)
    else:                               # if not first player
        suit = turn_cards[0].suit
        suit_cards = [card for card in player.hand if card.suit is suit]
        if len(suit_cards) != 0:    # if there is some suit card presents, selects it
            print 'suit card present'
            choice = random.choice(suit_cards)
        else:                           # if not suit card present, selects a random card
            print 'random choice!'
            choice = random.choice(player.hand)
    return choice
    