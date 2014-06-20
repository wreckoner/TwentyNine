'''
Created on Jun 10, 2014
@author: Dibyendu
'''

from Initiate.create import MakePlayers
from Classes.players import PlayersClass

def StartGame():
    return MakePlayers(numberOfHumans = 1, positions = [1])
    # For now we only consider 1 human and at the first position
    

def Run(status):
    while True:
        if status == "start":
            players = PlayersClass(StartGame())  # Create an object of PlayersClass
            status = "run"
            continue
        elif status == "run":
            flag = players.playOneTurn()
            if not flag: status = "stop"
        elif status == "stop":
            print "Game Finished!!!"
            break
    
    