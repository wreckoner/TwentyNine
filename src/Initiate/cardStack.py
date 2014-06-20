'''
Created on Jun 10, 2014
@author: Dibyendu
'''
##############################################################################################################
# This module defines generator function which returns a list called playDeck containing the playing card
# A playDeck is a deck of the 32 playable cards.
# Each card is an object with 4 attributes - suit, character, value, priority. 
##############################################################################################################
from Classes.cards import Card

def DeckGenerator():            #Generates play deck.
    suits = ["spades", "hearts", "diamonds", "clubs"]
    characters = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    # Note that 2 - 6 character cards are not used to play this game.
    values = [0, 0, 2, 1, 3, 0, 0, 1]
    priorities = [1, 2, 7, 5, 8, 3, 4, 6]
    playDeck = []
    for suit in suits:          # Loop generates deck of playing cards
        for (character, value, priority) in zip(characters[5:], values, priorities):
            playDeck.append(Card(suit, character, value, priority))
            
    return playDeck             # Returns the deck of playing cards
