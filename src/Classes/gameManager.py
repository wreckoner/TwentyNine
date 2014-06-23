'''
Created on Jun 22, 2014
@author: Dibyendu
'''
from Initiate.create import MakePlayers
import collections
import random
from GamePlay import scoreModule
import os

class GameManagerClass():
    '''
    This class manages the game.
    '''

    def __init__(self, params):
        self.initialize_variables()
        self.make_players()
        self.make_teams()
        self.bidding_by_players()
        
    def __repr__(self):
        return "%s | %s" %(self.team1, self.team2)
    
    def initialize_variables(self):
        self.played_cards = []
        self.previous_turn_cards = []
        self.bids = []
        self.trump_shown = False
    
    def make_players(self):
        self.players = MakePlayers(numberOfHumans = 1, positions = [1], parent = self)
        
    def make_teams(self):
        self.team1 = [player for player in self.players if player.index%2 is not 0]
        self.team1.append(0)
        self.team2 = [player for player in self.players if player not in self.team1]
        self.team2.append(0)
        
    def bidding_by_players(self):
        self.bring_to_front(random.choice(range(0, 4)))
        for player in self.players : self.bids.append(player.MakeBid())
        if not max(self.bids): self.bidding_by_players()
        else: self.bidder = self.players[self.bids.index(max(self.bids))]
        self.trump = self.bidder.SelectTrump()
        
    def play_one_turn(self):
        if len(self.players[0].hand) > 0:
            os.system("cls")
            self.played_cards += self.previous_turn_cards
            del self.previous_turn_cards[:]
            for player in self.players: player.ChooseCard(self.previous_turn_cards)
            print "played hand is - ",self.previous_turn_cards
            self.score_turn()
            print self.team1,self.team2
            return True
        else: return False
        
    def score_turn(self):
        scoreModule.ScoreHand(self)
    
    def bring_to_front(self, index):
        player_list = collections.deque(self.players)
        player_list.rotate(- index)
        self.players = list(player_list)
        