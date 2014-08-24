'''
Created on Aug 22, 2014
@author: Dibyendu, Dipayan
Contains display implementation of a bidding mechanism. (Not the bidding algorithm.)
'''

import pygame, copy, sys, display_engine

def bidding(players):
    '''Function to implement bidding by the players.'''
    screen = pygame.display.get_surface()                                       
    # Get a reference to the display surface
    screen_backup = pygame.Surface.copy(screen)                                 
    # Create a backup of original screen
    font = pygame.font.SysFont("mvboli", 50, 1, 0)
    max_bid = 15
    players = tuple(copy.copy(players))
    while len(players) > 1:
        passed = []      # A list of flags used to check which players have passed. Set to True if a player passes the bid
        for player in players:
            if player.index is 1:
                bid, trump = user_bidding(screen, font, max_bid, player)
                pygame.display.update(screen.blit(screen_backup, (0, 0)))
                if not bid:
                    message = font.render('You passed', 1, (0, 255, 255))
                    passed.append(True)
                else:
                    max_bid = bid
                    max_bidder = player
                    message = font.render('You bid %s.\n You selected %s as trump'%(bid, trump), 1, (0, 255, 255))
            else:
                bid, trump = player.make_bid(max_bid)
                if bid:
                    max_bid = bid
                    max_bidder = player
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
        players = [player for player, flag in zip(players, passed) if not flag]
        
    return max_bid, trump, max_bidder
                

def user_bidding(screen, font, max_bid, player):
    # Backup the original screen
    screen_original = pygame.Surface.copy(screen)
    # Create message surfaces
    text = font.render('State your bid:', 1, (0, 255, 255))
    message = pygame.Surface((text.get_rect().w, text.get_rect().h * 2), pygame.SRCALPHA, 32).convert_alpha()
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
    running = True
    while running:
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect_plus.collidepoint(pos) and bid < 28:
                    # When user clicks '>'
                    bid += 1
                    number = font.render('%s'%bid, 1, (0, 255, 255))
                    screen.blit(screen_backup, (0, 0))
                    screen.blit(number, number_rect)
                    pygame.display.update(rect)
                elif rect_minus.collidepoint(pos) and bid > max_bid + 1:
                    # When user clicks '<'
                    bid -= 1
                    number = font.render('%s'%bid, 1, (0, 255, 255))
                    screen.blit(screen_backup, (0, 0))
                    screen.blit(number, number_rect)
                    pygame.display.update(rect)
                elif rect_submit.collidepoint(pos):
                    # When user clicks 'BID'
                    pygame.display.update(screen.blit(screen_original, (0, 0)))
                    trump = select_trump(screen, font, player.hand, player.loc)
                    running = False
                elif rect_cease.collidepoint(pos):
                    # When user clicks 'PASS'
                    bid, trump = False, None
                    running = False
            elif event.type == pygame.QUIT:
                # When user clicks 'CLOSE' button
                running = False
                sys.exit()
    return bid, trump

def select_trump(screen, font, hand, loc):
    message = font.render('Select Trump', 1, (0, 255, 255))
    rect = message.get_rect()
    rect.center = screen.get_rect().center
    pygame.display.update(screen.blit(message, rect))
    while True:
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for card, loc in zip(hand[::-1], loc[::-1]):
                    if loc.collidepoint(pos):
                        return card.suit
            elif event.type is pygame.QUIT:
                sys.exit()