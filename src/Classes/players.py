'''
Created on Jun 13, 2014
@author: Dibyendu
'''
import collections
import random

class PlayersClass():
    '''
    This is a class of 4 players (Human/CPU)
    '''
    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]
        self.player3 = players[2]
        self.player4 = players[3]
        self.players = players
        self.previousHand = None
        self.makeTeams()
        self.bidding()
        
    def __repr__(self):
        return "Object of Four Players"
    
    def bidding(self):
        bids = []
        start = random.choice(range(0, 4))
        self.bringToFront(start)                            # Chooses a starting player randomly
        print "Round starts from :",self.players[0]
        for player in self.players:
            bids.append(player.MakeBid())
            print "%s has bid : %s"%(player, bids[-1] if bids[-1] != False else "Pass")
        self.bid = max(bids)
        self.bidder = self.players[bids.index(self.bid)]
        self.trump = self.bidder.SelectTrump()              # Highest bidder is called to select trump
        
    
    def playOneTurn(self):
        if len(self.player1.hand) > 0:                      # Checks if a player has any card left
            table = []
            for player in self.players:
                table = player.ChooseCard(table)
            self.previousTurn = table
            self.scoreTurn()
            print "The played Round is : ", table
            return True
        else:
            return False
        
    def scoreTurn(self):
        #scoreModule.ScoreHand(self.players, self.previousTurn, self.trump, self.team1, self.team2)
        pass
    
    def bringToFront(self, index):
        # Brings the player at given index to the front while maintaining order of the players.
        temp = collections.deque(self.players)
        temp.rotate(- index)
        self.players = list(temp)
        
    def makeTeams(self):
        self.team1 = [self.player1, self.player3, 0]
        self.team2 = [self.player2, self.player4, 0]