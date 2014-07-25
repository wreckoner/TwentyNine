'''
Created on Jul 14, 2014
@author: Dibyendu
'''

import pygame
from pygame.locals import HWACCEL, SWSURFACE
from display_engine.methods import load_image
from display_engine import deal_module, menu_module, select_card_module
from display_engine.reset_display import reset_display

class display_manager():
    def __init__(self):
        self.image_dict = self.init()
    
    def init(self):
        # Initiates essential features, return image dictionary
        pygame.init()
        self.image_dict = {}
        self.image_dict['screen'] = pygame.display.set_mode((800, 600), HWACCEL | SWSURFACE)
        pygame.display.set_caption("Twenty Nine")
        self.image_dict['background'] = load_image('table_cloth.jpg', ['images'])
        self.image_dict['background'] = pygame.transform.scale(self.image_dict['background'], self.image_dict['screen'].get_rect().size)
        self.image_dict['screen'].blit(self.image_dict['background'], (0, 0))
        pygame.display.flip()
        return self.image_dict
    
    def start_menu(self):
        # This will have the start menu of the game. For now starts directly into the game
        return menu_module.menu_screen(self.image_dict)
    
    def draw_players(self, players):
        deal_module.deal_cards(players, self.image_dict['screen'])
        
    def play_one_turn(self, players, pos):
        return select_card_module.select_a_card(players, self.image_dict['screen'], self.image_dict['background'])
        #user_animation(players[0], self.image_dict['screen'], self.image_dict['background'], pos)
        
    def reset_display(self, players, table_reset = False):
        reset_display(players, self.image_dict['screen'], self.image_dict['background'], table_reset)
        
    
        