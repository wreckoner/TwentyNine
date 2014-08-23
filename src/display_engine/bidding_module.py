'''
Created on Aug 22, 2014
@author: Dibyendu, Dipayan
Contains display implementation of a bidding mechanism. (Not the bidding algorithm.)
'''

import pygame

def bidding(players):
    screen = pygame.display.get_surface()
    screen_backup = pygame.Surface.copy(screen)
    font = pygame.font.SysFont("Arial", 50, 1, 0)
    message = font.render('State your bid.', 1, (255, 0, 0), (255, 255, 255))
    max_bid = 16
    for player in players:
        if player.index != 1:
            bid, trump = player.make_bid(max_bid)
            if bid:
                max_bid = bid
                max_bidder = player
                trump = trump
                message = font.render('%s has bid %s.'%(player, bid), 1, (255, 0, 0), (255, 255, 255))
            else:
                message = font.render('%s has passed.'%player, 1, (255, 0, 0), (255, 255, 255))
        
        pos = message.get_rect()
        pos.center = screen.get_rect().center
        pygame.display.update(screen.blit(message, pos))
        pygame.time.delay(2000)
        pygame.display.update(screen.blit(screen_backup, (0, 0)))
        
    return max_bid, trump, max_bidder
                