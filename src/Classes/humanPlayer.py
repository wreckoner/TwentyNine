'''
Created on Jun 11, 2014

@author: Dibyendu
'''

class HumanPlayerClass():
    '''
    This is a Human player class. Takes a list of cards as parameter
    '''
    def __init__(self, hand, index):
        self.hand = sorted(hand,key = lambda x : x.suit)
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
    
    def ChooseCard(self, table):
        #TODO: Write a method.
        print "Choose a card from your hand : ",self.hand
        i = raw_input("Enter index number : ")
        choice = self.hand[int(i)]
        table.append(choice)
        self.hand.remove(choice)
        return table
        