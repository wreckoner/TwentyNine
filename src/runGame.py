'''
Created on Jun 10, 2014
@author: Dibyendu
'''

from Initiate.create import MakePlayers
from Classes import gameManager

def StartGame():
    return MakePlayers(numberOfHumans = 1, positions = [1], parent = None)
    # For now we only consider 1 human and at the first position
    

def Run(status):
    while True:
        if status == "start":
            game = gameManager.GameManagerClass(None)
            status = "run"
        elif status == "run":
            flag = game.play_one_turn()
            if not flag: status = "stop"
        elif status == "stop":
            print "Game Finished!!!"
            break
        raw_input("press enter to proceed")
    
    