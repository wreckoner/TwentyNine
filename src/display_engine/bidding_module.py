'''
Created on Aug 22, 2014
@author: Dibyendu, Dipayan
Contains display implementation of a bidding mechanism. (Not the bidding algorithms of the AI.)
'''

import pygame, copy, sys, display_engine

def bidding(players):
    '''Function to implement bidding by the players.'''
    time_delay = 1000           # Time in milliseconds between bids by cpu
    screen = pygame.display.get_surface()                                       
    # Get a reference to the display surface
    screen_backup = pygame.Surface.copy(screen)                                 
    # Create a backup of original screen
    font = pygame.font.SysFont("rockwell extra", 50, 1, 0)
    max_bid = 15
    players = tuple(copy.copy(players))
    while len(players) > 1:
        passed = []      # A list of flags used to check which players have passed. Set to True if a player passes the bid
        for player in players:
            bid = player.make_bid(max_bid)
            pygame.display.update(screen.blit(screen_backup, (0, 0)))
            if bid:
                max_bid = bid
                max_bidder = player
                message = font.render('player %s has bid %s'%(player.index, bid), 1, (136, 255, 0))
                passed.append(False)
            else:
                message = font.render('player %s has passed'%player.index, 1, (136, 255, 0))
                passed.append(True)
            pos = message.get_rect()
            pos.center = screen.get_rect().center
            pygame.display.update(screen.blit(message, pos))
            pygame.time.delay(time_delay)
            pygame.display.update(screen.blit(screen_backup, (0, 0)))
        players = [player for player, flag in zip(players, passed) if not flag]
    if max_bid is 15:
        # If all the players pass
        max_bid, trump, max_bidder = False, False, False
        restart_deal_display()
    else:
        trump = max_bidder.select_trump()
    return max_bid, trump, max_bidder



def user_bidding(player, max_bid):
    ''' Function asks the user to enter or pass bid.
        Called by the make_bid(self, max_bid) function of humanPlayer class'''
    # Initialize, load resources
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont("rockwell extra", 50, 1, 0)
    message_src = display_engine.methods.load_image('messages.png', ['images'], 1)
    # Backup the original screen
    screen_original = pygame.Surface.copy(screen)
    # Create message surfaces
    text = pygame.Surface((520, 50), pygame.SRCALPHA, 32).convert_alpha()
    text.blit(message_src, (0, 0), (6, 14, 520, 48))
    message = pygame.Surface((text.get_rect().w, text.get_rect().h * 3), pygame.SRCALPHA, 32).convert_alpha()
    message.blit(text, (0, 0))
    pos = message.get_rect()
    pos.center = screen.get_rect().center
    rect = screen.blit(message, pos)
    # Loading buttons
    plus = pygame.Surface((45, 41), pygame.SRCALPHA, 32).convert_alpha()
    plus.blit(message_src, (0, 0), (370, 370, 45, 41))
    minus = pygame.Surface((45, 41), pygame.SRCALPHA, 32).convert_alpha()
    minus.blit(message_src, (0, 0), (288, 370, 45, 41))
    submit = pygame.Surface((123, 55), pygame.SRCALPHA, 32).convert_alpha()
    submit.blit(message_src, (0, 0), (5, 69, 123, 55))
    submit = pygame.transform.rotozoom(submit, 0, 0.8)
    cease = pygame.Surface((154, 55), pygame.SRCALPHA, 32).convert_alpha()
    cease.blit(message_src, (0, 0), (166, 69, 154, 45))
    cease = pygame.transform.rotozoom(cease, 0, 0.8)
    # Blit Plus and Minus buttons
    rect_minus = minus.get_rect()
    rect_minus.center = rect.topleft
    rect_minus = rect_minus.move(message.get_rect().w/3, message.get_rect().h*2/3)
    screen.blit(minus, rect_minus)
    rect_plus = plus.get_rect()
    rect_plus.center = rect.topleft
    rect_plus = rect_plus.move(message.get_rect().w*2/3, message.get_rect().h*2/3)
    screen.blit(plus, rect_plus)
    # Blit buttons
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
    number = font.render('%s'%bid, 1, (136, 255, 0))
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
                    number = font.render('%s'%bid, 1, (136, 255, 0))
                    screen.blit(screen_backup, (0, 0))
                    screen.blit(number, number_rect)
                    pygame.display.update(rect)
                elif rect_minus.collidepoint(pos) and bid > max_bid + 1:
                    # When user clicks '<'
                    bid -= 1
                    number = font.render('%s'%bid, 1, (136, 255, 0))
                    screen.blit(screen_backup, (0, 0))
                    screen.blit(number, number_rect)
                    pygame.display.update(rect)
                elif rect_submit.collidepoint(pos):
                    # When user clicks 'BID'
                    pygame.display.update(screen.blit(screen_original, (0, 0)))
                    running = False
                elif rect_cease.collidepoint(pos):
                    # When user clicks 'PASS'
                    bid  = False
                    running = False
            elif event.type == pygame.QUIT:
                # When user clicks 'CLOSE' button
                running = False
                sys.exit()
    return bid


def select_trump_by_user(player):
    '''This function asks the user to select a card from his hand for the trump.
       Takes a reference to the screen, font, user's hand and user's card loc as arguements'''
    screen = pygame.display.get_surface()
    screen_backup = pygame.Surface.copy(screen)
    message_src = display_engine.methods.load_image('messages.png', ['images'], 1)
    message = pygame.Surface((537, 50), pygame.SRCALPHA, 32).convert_alpha()
    message.blit(message_src, (0, 0), (8, 131, 537, 50))
    rect = message.get_rect()
    rect.center = screen.get_rect().center
    pygame.display.update(screen.blit(message, rect))
    
    suits = {}
    
    suits['spades'] = pygame.Surface((50, 50), pygame.SRCALPHA, 32).convert_alpha()
    suits['spades'].blit(message_src, (0, 0), (421, 357, 50, 50))
    suits['hearts'] = pygame.Surface((50, 50), pygame.SRCALPHA, 32).convert_alpha()
    suits['hearts'].blit(message_src, (0, 0), (477, 357, 50, 50))
    suits['diamonds'] = pygame.Surface((50, 50), pygame.SRCALPHA, 32).convert_alpha()
    suits['diamonds'].blit(message_src, (0, 0), (535, 357, 50, 50))
    suits['clubs'] = pygame.Surface((50, 50), pygame.SRCALPHA, 32).convert_alpha()
    suits['clubs'].blit(message_src, (0, 0), (591, 357, 50, 50))
    
    message_2 = pygame.Surface((440, 48), pygame.SRCALPHA, 32).convert_alpha()
    message_2.blit(message_src, (0, 0), (5, 419, 440, 48))
    accept = pygame.Surface((245, 48), pygame.SRCALPHA, 32).convert_alpha()
    accept.blit(message_src, (0, 0), (450, 420, 245, 48))
    rect_accept = pygame.Rect(-10, -10, 0, 0)
    
    hand, loc = player.hand, player.loc
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect_accept.collidepoint(pos):
                    running = False
                else:
                    for card, point in zip(reversed(hand), reversed(loc)):
                        if point.collidepoint(pos):
                            trump = card.suit
                            pygame.display.update(screen.blit(screen_backup, (0, 0)))
                            rect = message_2.get_rect()
                            rect.midbottom = screen.get_rect().center
                            rect_suit = suits[trump].get_rect()
                            rect_suit.midtop = rect.midbottom
                            rect_accept = accept.get_rect()
                            rect_accept.midtop = rect_suit.midbottom
                            pygame.display.update((screen.blit(message_2, rect), screen.blit(suits[trump], rect_suit), screen.blit(accept, rect_accept)))
            elif event.type is pygame.QUIT:
                sys.exit()
    pygame.display.update(screen.blit(screen_backup, (0, 0)))
    return trump

def restart_deal_display():
    '''Called by bidding(max_bid) if all the players have passed
       Informs the players that the cards are going to be dealt again.'''
    screen = pygame.display.get_surface()
    message_src = display_engine.methods.load_image('messages.png', ['images'], 1)
    message = pygame.Surface((570, 55), pygame.SRCALPHA, 32).convert_alpha()
    message.blit(message_src, (0, 0), (8, 473, 570, 55))
    trail = pygame.Surface((484, 55), pygame.SRCALPHA, 32)
    trail.blit(message_src, (0, 0), (8, 533, 484, 55))
    rect = message.get_rect()
    rect.center = screen.get_rect().center
    rect_trail = trail.get_rect()
    rect_trail.topleft = rect.bottomleft
    pygame.display.update((screen.blit(message, rect), screen.blit(trail, rect_trail)))
    pygame.time.delay(1500)