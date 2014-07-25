'''
Created on Jul 14, 2014
@author: Dibyendu
'''
import random
from Classes.humanPlayer import HumanPlayerClass
from Classes.computerPlayer import ComputerPlayerClass
from Initiate.cardStack import shuffle_deck

class game_manager():
    def __init__(self, parent):
        self.parent = parent
        self.init()
        self.make_players()
        #self.start_new_round()
    
    def init(self):
        self.players = []               # Holds the list of four players
        self.cards = shuffle_deck()     # List of cards. During a round the played cards are added after every turn
        self.played_turn = []           # Holds the cards being played in a single turn
        self.bidder = None              # Holds the highest bidding player
        self.trump_shown = False        # Flag for whether trump is shown or not 
        self.trump = None               # Holds the trump suit
        self.round_ended = False        # Becomes True when round ends. Used to start next round.
        self.turns = 0                  # Counter to keep track of number of turns being played. Maxes to 8
                
    def start_new_round(self):
        self.deal_first_four_cards()
        self.bidding()
        self.deal_last_four_cards()
    
    def make_players(self):
        for index in xrange(1, 5):
            self.players.append(HumanPlayerClass(None , index, self) if index is 1 else ComputerPlayerClass(None, index, self))
            
    def deal_first_four_cards(self):
        for player in self.players: 
            player.hand = [self.cards.pop(0) for _ in xrange(4)]
            player.sort_hand()
            
    def deal_last_four_cards(self):
        for player in self.players:
            player.hand += [self.cards.pop(0) for _ in xrange(4) if len(self.cards)]
            player.sort_hand()
    
    def make_teams(self):
        self.team1 = [player for player in self.players if player.index%2 is not 0]
        self.team1.append(0)
        self.team2 = [player for player in self.players if player not in self.team1]
        self.team2.append(0)
        
    def bidding(self):
        return
        # need to implement a bidding proccess.
        self.bring_to_front(random.choice(range(0, 4)))
        for player in self.players : self.bids.append(player.MakeBid())
        if not max(self.bids): self.bidding_by_players()
        else: self.bidder = self.players[self.bids.index(max(self.bids))]
        self.bidder.SelectTrump()
    
    def play_one_turn(self):
        if self.turns < 8:
            for player in self.players:
                player.choose_card(self.played_turn)
            self.turns += 1
            return True
        elif self.turns is 8: return False
        
    def score_turn(self):
        pass