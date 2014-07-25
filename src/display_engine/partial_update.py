'''
Created on Jul 17, 2014
@author: Dibyendu
'''
from display_engine.image_files import card_files
import pygame


def get_area_of_player(index):
    '''Returns a rect object of the surface occupied by the cards of one of the four players. 
    Useful for redrawing the hand of a single player, rather than the whole screen '''
    screen_x, screen_y = pygame.display.get_surface().get_rect().size
    boundary_offset = 0.30
    bottom_offset = 0.05
    #card = card_files()['clubs - A']    # Used as a sample to measure the dimensions
    card_width, card_height = pygame.transform.rotozoom(pygame.Surface((72, 96)), 0, 1.3).get_rect().size
    if index is 1:
        left = int(boundary_offset * screen_x) - 10
        top = int( screen_y * (1 - bottom_offset) - card_height - 10)
        width = int( screen_x * ( 1 - 2 * boundary_offset) + 20)
        height = card_height + 20
        rect = pygame.Rect(left, top, width, height)
    elif index is 2:
        left = int(bottom_offset * screen_x) - 10
        top = int( boundary_offset *  screen_y) - 10
        width = card_height + 20
        height = int (screen_x * (1 - 2 * boundary_offset) + 20)
        rect = pygame.Rect(left, top, width, height)
    elif index is 3:
        left = int(boundary_offset * screen_x) - 10
        top = int(screen_y * bottom_offset) - 10
        width = int( screen_x * ( 1 - 2 * boundary_offset) + 20)
        height = card_height + 20
        rect = pygame.Rect(left, top, width, height)
    elif index is 4:
        left = int( (1 - bottom_offset) * screen_x - card_height) - 10
        top = int( boundary_offset *  screen_y) - 10
        width = card_height + 20
        height = int (screen_x * (1 - 2 * boundary_offset) + 20)
        rect = pygame.Rect(left, top, width, height)
    return rect