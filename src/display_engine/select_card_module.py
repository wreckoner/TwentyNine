'''
Created on Jul 18, 2014
@author: Dibyendu
This module contains methods to animate user's interaction with his/her cards. Specifically
If a card is clicked once, it is moved up by a few pixels. If it is clicked again it is played. If it is right clicked or if some other area is card is clicked that is selected.
'''
import pygame
from display_engine.draw_selected_cards_module import draw_selected_card
from display_engine.draw_players import draw_player

def select_a_card(player, screen, background):
    '''
    This method sets up an event handler for handling the selection of card by the user
    for playing.
    '''
    index = 8
    running = True
    flag = False
    while running:
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                flag, index = user_animation(player, screen, background, pos, index)
                if flag: running = False
    return index
        

def user_animation(user, screen, background, pos, clicked):
    for card_pos, index in zip(list(reversed(user.loc)), list(reversed(xrange(len(user.hand))))):
        if card_pos.collidepoint(pos):
            if clicked is index:                 # True if the card has been clicked before
                return True, index
            elif clicked is not index:           # If not clicked before, calls animation method and sets clicked index
                draw_player(user, screen, background, index, True)
                clicked = index
                break
    return False, index