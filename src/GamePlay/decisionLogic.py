'''
@author : Dibyendu Das
This module contains the decision logics of the computer players
'''
import random


def RandomCardSelect(hand, table):              # This method is a random card selector.
    if len(table) == 0:                         # Checks to see if it is the first player in the turn
        choice = random.choice(hand)
    else:                                       # Searches for cards of the played suit and selects
        suitCards = [card for card in hand if card.suit == table[0].suit]
        if len(suitCards) > 0: 
            choice = random.choice(suitCards)
        else:                                   # If there are no suit cards, chooses a random card
            choice = random.choice(hand)
    hand.remove(choice)
    table.append(choice)
    return (hand, table)