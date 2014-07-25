'''
Created on Jul 24, 2014
@author: Dibyendu
'''
import pygame
from display_engine.image_files import card_files
from display_engine.methods import load_image
from display_engine.partial_update import get_area_of_player

def blit_background(screen, background):
    '''Blits the background image on display. Pass the background and screen as references'''
    pygame.display.update(screen.blit(background, (0, 0)))
    
def blit_middle_deck(screen, card_scale):
    '''Blits the remaining card deck on the middle of the screen/table.'''
    image = card_files()['back - up']
    image = load_image(image)
    image = pygame.transform.rotozoom(image, 180, 1.3)
    rect = image.get_rect()
    rect.center = screen.get_rect().center
    pygame.display.update(screen.blit(image, rect))
    
def blit_turn(turn, screen, card_scale, start = 0):
    '''blits the cards played in a turn'''
    for card, index in zip(turn, xrange(1, 5)):
        if index is 1:
            image = pygame.transform.rotozoom(load_image(card.image_file), 0, card_scale)
            image_rect = image.get_rect()
            image_rect.midtop = screen.get_rect().center
            pygame.display.update(screen.blit(image, image_rect))
        elif index is 2:
            image = pygame.transform.rotozoom(load_image(card.image_file), 0, card_scale)
            image_rect = image.get_rect()
            image_rect.midright = screen.get_rect().center
            pygame.display.update(screen.blit(image, image_rect))
        elif index is 3:
            image = pygame.transform.rotozoom(load_image(card.image_file), 0, card_scale)
            image_rect = image.get_rect()
            image_rect.midbottom = screen.get_rect().center
            pygame.display.update(screen.blit(image, image_rect))
        elif index is 4:
            image = pygame.transform.rotozoom(load_image(card.image_file), 0, card_scale)
            image_rect = image.get_rect()
            image_rect.midleft = screen.get_rect().center
            pygame.display.update(screen.blit(image, image_rect))
        
def erase_hand(player_index, screen, background):
    ''' erases the players cards from the table, depending on the player index'''
    rect = get_area_of_player(player_index)
    pygame.display.update(screen.blit(background, rect.topleft, rect))
        