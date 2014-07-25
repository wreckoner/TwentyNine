'''
Created on Jun 11, 2014
@author: Dibyendu
'''

class HumanPlayerClass():
    '''
    This is a Human player class. Takes a list of cards as parameter
    '''
    def __init__(self, hand, index, parent):
        self.hand = hand
        self.parent = parent
        self.index = index
        self.trump = False
        self.loc = []
        self.clicked = 8        # Used to keep track of which card has been selected
        self.selected_card_index = 8
    
    def __repr__(self):
        return "Human %s" %self.index
    
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
    
    def choose_card(self):
        # redundant method in graphic game, since card selection is done graphically.
        choice = self.hand[self.selected_card_index]
        self.parent.played_turn.append(choice)
        self.hand.remove(choice)
        print 'you played', choice
        self.selected_card_index, self.clicked = 8, 8
        
    def sort_hand(self):
        self.hand = sorted(self.hand, key = lambda x : (x.sort_key, x.priority ))