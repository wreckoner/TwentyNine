'''
Created on Jun 11, 2014

@author: Dibyendu
'''
from Display import PrintToConsole

class HumanPlayerClass():
    '''
    This is a Human player class. Takes a list of cards as parameter
    '''
    def __init__(self, hand, index, parent):
        self.hand = sorted(hand,key = lambda x : x.suit)
        self.parent = parent
        self.index = index
        self.trump = False
    
    def __repr__(self):
        return "Human. ID - %s" %self.index
    
    def MakeBid(self):
        print "Your hand is :",self.hand
        bid = raw_input("Enter a bid between 16 and 22, or press return to pass to the next user.")
        if bid.isdigit():
            return int(bid)
        else:
            return False
    
    def SelectTrump(self):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        index = raw_input("%s. Enter the index of the suit you want to select as trump : "%(suits))
        self.trump = suits[int(index)]
        return self.trump
    
    def ChooseCard(self, turn_cards):
        PrintToConsole.print_to_console(("Choose a card from your hand - %s : " %self.hand))
        i = raw_input("Enter index number : ")
        choice = self.hand[int(i)]
        turn_cards.append(choice)
        self.hand.remove(choice)
        return turn_cards
        