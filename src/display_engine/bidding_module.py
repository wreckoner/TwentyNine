'''
Created on Aug 22, 2014
@author: Dibyendu, Dipayan
Contains display implementation of a bidding mechanism. (Not the bidding algorithm.)
'''

import pygame
import copy
import sys
import display_engine

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
                #message = font.render('State your bid:', 1, (255, 0, 0), (255, 255, 255))
                user_bidding(screen, font, max_bid)
                passed.append(False)
            else:
                bid, trump = player.make_bid(max_bid)
                if bid:
                    max_bid = bid
                    max_bidder = player
                    trump = trump
                    message = font.render('player %s has bid %s'%(player.index, bid), 1, (0, 255, 255))
                    passed.append(False)
                else:
                    message = font.render('player %s has passed'%player.index, 1, (0, 255, 255))
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
                

def user_bidding(screen, font, max_bid):
    # Create message surfaces
    text = font.render('State your bid:', 1, (0, 255, 255))
    message = pygame.Surface((text.get_rect().w, text.get_rect().h * 2), pygame.SRCALPHA, 32).convert_alpha()
    #message.fill((255, 255, 255))
    message.blit(text, (0, 0))
    pos = message.get_rect()
    pos.center = screen.get_rect().center
    rect = screen.blit(message, pos)
    # Loading buttons
    buttons = display_engine.methods.load_image('bid_buttons.png', ['images'], 1)
    plus = pygame.Surface((75, 75), pygame.SRCALPHA, 32).convert_alpha()
    plus.blit(buttons, (0, 0), (115, 5, 65, 70))
    plus = pygame.transform.rotozoom(plus, 0, 0.6)
    minus = pygame.Surface((75, 75), pygame.SRCALPHA, 32).convert_alpha()
    minus.blit(buttons, (0, 0), (0, 5, 65, 70))
    minus = pygame.transform.rotozoom(minus, 0, 0.6)
    submit = pygame.Surface((75, 40), pygame.SRCALPHA, 32).convert_alpha()
    submit.blit(buttons, (0, 0), (0, 110, 75, 40))
    cease = pygame.Surface((100, 45), pygame.SRCALPHA, 32).convert_alpha()
    cease.blit(buttons, (0, 0), (80, 101, 100, 45))
    # Blit Plus and Minus buttons
    #plus = font.render('+', 1, (255, 0, 0))
    #minus = font.render('-', 1, (255, 0, 0))
    rect_minus = minus.get_rect()
    rect_minus.center = rect.topleft
    rect_minus = rect_minus.move(message.get_rect().w/3, message.get_rect().h*2/3)
    screen.blit(minus, rect_minus)
    rect_plus = plus.get_rect()
    rect_plus.center = rect.topleft
    rect_plus = rect_plus.move(message.get_rect().w*2/3, message.get_rect().h*2/3)
    screen.blit(plus, rect_plus)
    # Blit buttons
    #submit = font.render('Bid', 1, (255, 0, 0))
    #cease = font.render('Pass', 1, (255, 0, 0))
    rect_submit = submit.get_rect()
    rect_submit.bottomleft = rect.bottomleft
    screen.blit(submit, rect_submit)
    rect_cease = cease.get_rect()
    rect_cease.bottomright = rect.bottomright
    screen.blit(cease, rect_cease)
    # Create a backup of the screen without any numbers displayed
    screen_backup = pygame.Surface.copy(screen)
    # Blit number
    bid = max_bid + 1
    number = font.render('%s'%bid, 1, (0, 255, 255))
    number_rect = number.get_rect()
    number_rect.center = rect.topleft
    number_rect = number_rect.move(message.get_rect().w/2, message.get_rect().h*2/3)
    screen.blit(number, number_rect)
    # Update display
    pygame.display.update(rect)
    # Wait for input event from user to receive the bid.
    while True:
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect_plus.collidepoint(pos) and bid < 28:
                    # When user clicks >
                    bid += 1
                    number = font.render('%s'%bid, 1, (0, 255, 255))
                    screen.blit(screen_backup, (0, 0))
                    screen.blit(number, number_rect)
                    pygame.display.update(rect)
                elif rect_minus.collidepoint(pos) and bid > max_bid + 1:
                    # When user clicks <
                    bid -= 1
                    number = font.render('%s'%bid, 1, (0, 255, 255))
                    screen.blit(screen_backup, (0, 0))
                    screen.blit(number, number_rect)
                    pygame.display.update(rect)
                elif rect_submit.collidepoint(pos):
                    print 'you pressed bid'
                elif rect_cease.collidepoint(pos):
                    print 'you pressed pass'
            elif event.type == pygame.QUIT:
                sys.exit()
    return bid