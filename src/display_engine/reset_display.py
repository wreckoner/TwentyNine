'''
Created on Jul 17, 2014
@author: Dibyendu
This module contains a reset function. It will reset the background and if required redraw the table, depending on the cards present. Same as the deal card code, except time delay is put to zero
'''

import pygame
from display_engine.methods import load_image
from display_engine.image_files import card_files
from display_engine.partial_update import get_area_of_player

def reset_display(players, screen, background, table_reset = False):
    reset_background(screen, background)
    if table_reset:
        reset_cards(players, screen)
        pygame.display.update([get_area_of_player(1), get_area_of_player(2), get_area_of_player(3), get_area_of_player(4)])

def reset_background(screen, background):
    pygame.display.update(screen.blit(background, (0, 0)))

def reset_cards(players, screen):
    
    card_scale = 1.3            # Scaling factor of card drawn
    boundary_offset = 0.30      # 20% of screen on both sides
    bottom_offset = 0.05        # 10% of screen from the bottom
    
    ###### This code segment displays the back of a card at the center of the table, as a prop########
    pygame.display.update()
    card_back = pygame.transform.rotozoom(load_image(card_files()['back - up']), 180, card_scale)
    card_rect = card_back.get_rect()
    card_rect.center = screen.get_rect().center
    screen.blit(card_back, card_rect)
    pygame.display.update(card_rect)
    ##################################################################################################
    if len(players[0].hand) == 0: # if there are no cards in hand, nothing to draw.
        return
    
    for player in players:
        if player.index is 1: deal_user_cards(player, screen, card_scale, boundary_offset, bottom_offset)
        elif player.index is 2: deal_second_player(player, screen, card_scale, boundary_offset, bottom_offset)
        elif player.index is 3: deal_third_player(player, screen, card_scale, boundary_offset, bottom_offset)
        elif player.index is 4: deal_fourth_player(player, screen, card_scale, boundary_offset, bottom_offset)


def deal_user_cards(player, screen, card_scale, boundary_offset, bottom_offset):
    
    ##########################Load the images, scale and rotate them as required######################
    images = [card.image_file for card in player.hand]
    images = map(load_image, images)
    scale = [card_scale for _ in xrange(len(player.hand))]
    angle = [180 for _ in xrange(len(player.hand))]
    images = map(pygame.transform.rotozoom, images, angle, scale)   # List of images to be blitted
    ##################################################################################################
    
    screen_size = screen.get_rect().size
    card_width, card_height = images[0].get_rect().size
    loc = []
    
    ############################If there is a single cards blits it at the center#####################
    if len(images) == 1:
        rect = images[0].get_rect()
        rect.midtop = (screen.get_rect().centerx, int(screen_size[1] - float(bottom_offset * screen_size[1]) - card_height))
        screen.blit(images[0], rect)
        loc.append(rect)
        player.loc = loc
        return
    
    ####################################Calculating the x and y positions and increments##############
    x = int(boundary_offset * screen_size[0])
    y = int(screen_size[1] - float(bottom_offset * screen_size[1]) - card_height)
    x_increment = int( float(screen_size[0] * (1 - 2 * boundary_offset) - card_width)/float( len(images) - 1 ) )
    
    ##################################################################################################
    
    for card in images:
        rect = screen.blit(card, (x, y))
        loc.append(rect)
        x += x_increment
    
    player.loc = loc    #Adds an attribute loc in the player object which contains rects of all cards
    
    
    
def deal_second_player(player, screen, card_scale, boundary_offset, bottom_offset):
    
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - side'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    
    ############################If there is a single cards blits it at the center#####################
    if len(player.hand) == 1:
        rect = card.get_rect()
        rect.midleft = ( int(screen.get_rect().width * bottom_offset), screen.get_rect().centery)
        screen.blit(card, rect)
        return
    
    ####################################Calculating the x and y positions and increments##############
    x = int(bottom_offset * screen_size[0])
    y = int(boundary_offset * screen_size[1])
    y_increment = int(float(screen_size[1] * (1 - 2 * boundary_offset)-card.get_rect().height)/float(len(player.hand)-1))
    ##################################################################################################
        
    for _ in xrange(len(player.hand)):
        screen.blit(card, (x, y))
        y += y_increment

def deal_third_player(player, screen, card_scale, boundary_offset, bottom_offset):
    
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - up'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    ############################If there is a single cards blits it at the center#####################
    if len(player.hand) == 1:
        rect = card.get_rect()
        rect.midtop = ( screen.get_rect().centerx, int(screen.get_rect().height * bottom_offset))
        screen.blit(card, rect)
        return
    
    ####################################Calculating the x and y positions and increments##############
    x = int(boundary_offset * screen_size[0])
    y = int(bottom_offset * screen_size[1])
    x_increment = int(float(screen_size[0]*(1 - 2 * boundary_offset) - card.get_rect().width)/float(len(player.hand) - 1) )
    ##################################################################################################
    
    for _ in xrange(len(player.hand)):
        screen.blit(card, (x, y))
        x += x_increment
        

def deal_fourth_player(player, screen, card_scale, boundary_offset, bottom_offset):
    
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - side'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    
    ############################If there is a single cards blits it at the center#####################
    if len(player.hand) == 1:
        rect = card.get_rect()
        rect.midright = ( int(screen.get_rect().width * (1 - bottom_offset)), screen.get_rect().centery)
        screen.blit(card, rect)
        return
    
    ####################################Calculating the x and y positions and increments##############
    x = int( (1 - bottom_offset) * screen_size[0] - card.get_rect().width)
    y = int(boundary_offset * screen_size[1])
    y_increment = int(float(screen_size[1] * (1 - 2 * boundary_offset) - card.get_rect().height)/float(len(player.hand)-1))
    ##################################################################################################
    
    for _ in xrange(len(player.hand)):
        screen.blit(card, (x, y))
        y += y_increment