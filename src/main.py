'''
Created on Jun 10, 2014
@author: Dibyendu

Source code of Twenty Nine
Some terminologies  used in the code:

hand - The cards held by one player
deal - Distributing the cards
'''
from Classes.overseer import overseer

if __name__ == '__main__':
    game = overseer()
    game.run()
    