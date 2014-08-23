'''
Created on Aug 22, 2014
@author: Dibyendu, Dipayan
Contains display implementation of a bidding mechanism. (Not the bidding algorithm.)
'''

import pygame
import copy

def bidding(players):
    screen = pygame.display.get_surface()                                       # Gets a reference to the display surface
    screen_backup = pygame.Surface.copy(screen)                                 # Creates a backup of display surface
    font = pygame.font.SysFont("mvboli", 50, 1, 0)
    max_bid = 16
    players = tuple(copy.copy(players))
    while len(players) > 1:
        passed = []      # A list of flags used to check which players have passed.
        for player in players:
            if player.index is 1:
                message = font.render('State your bid:', 1, (255, 0, 0), (255, 255, 255))
                passed.append(False)
            else:
                bid, trump = player.make_bid(max_bid)
                if bid:
                    max_bid = bid
                    max_bidder = player
                    trump = trump
                    message = font.render('player %s has bid %s'%(player.index, bid), 1, (255, 0, 0), (255, 255, 255))
                    passed.append(False)
                else:
                    message = font.render('player %s has passed'%player.index, 1, (255, 0, 0), (255, 255, 255))
                    passed.append(True)
            pos = message.get_rect()
            pos.center = screen.get_rect().center
            pygame.display.update(screen.blit(message, pos))
            pygame.time.delay(2000)
            pygame.display.update(screen.blit(screen_backup, (0, 0)))
            print passed
        players = [player for player, flag in zip(players, passed) if not flag]
        print players
        
        
    return max_bid, trump, max_bidder
                