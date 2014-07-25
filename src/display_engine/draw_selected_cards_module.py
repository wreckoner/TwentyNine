'''
Created on Jul 18, 2014
@author: Dibyendu
'''
from display_engine.methods import load_image
import pygame


def draw_selected_card(index, screen, card):
    '''Draws the selected card passed to this function to the center of the table
    close to the player who has played it. Position depends on the index of the player,
    starting from 1 for user.'''
    card_scale = 1.3
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