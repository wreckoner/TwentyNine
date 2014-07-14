'''
Created on Jun 11, 2014
@author: Dibyendu
'''

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
        bid = raw_input("Enter a bid greater than any previous bid with a minimum of 16, or press return to pass to the next user : ")
        if bid.isdigit():
            return int(bid)
        else:
            return False
    
    def SelectTrump(self):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        index = raw_input("%s. Enter the index of the suit you want to select as trump : "%(suits))
        self.parent.trump = suits[int(index)]
    
    def ChooseCard(self, turn_cards):
        i = raw_input("Your hand is %s. Enter index number of the card you choose. Or press enter to reveal trump : "%self.hand)
        if not i.isdigit():
            self.parent.trump_shown = True
            i = raw_input("Now enter the index number of your desired card : ")
        choice = self.hand[int(i)]
        turn_cards.append(choice)
        self.hand.remove(choice)
        