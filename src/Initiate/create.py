'''
Created on Jun 13, 2014
@author: Dibyendu
'''

from Initiate.dealCards import DealHands
from Initiate.cardStack import DeckGenerator
from Classes.humanPlayer import HumanPlayerClass
from Classes.computerPlayer import ComputerPlayerClass

def MakePlayers(numberOfHumans, positions):
    # Method makes four player objects and passes them as a list.
    players = []
    for index, hand in zip(range(1, 5), DealHands(DeckGenerator())):    # Iterate over the list of hands.
        if index in positions:
            players.append(HumanPlayerClass(hand, index))
        else:
            players.append(ComputerPlayerClass(hand, index))
    return players