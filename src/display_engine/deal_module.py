'''
Created on Jul 15, 2014
@author: Dibyendu

This module contains the animation for dealing cards to the players at the start of every round.
Dealing starts from 1st player (user) to 2,3 and 4, in clockwise direction.
The method is passed a reference to player object. 
The player object has a hand attribute which is a list of card objects. 
Each card object has an attribute called image_file which is the path to the file.
'''
import pygame
from display_engine.methods import load_image
from display_engine.image_files import card_files

def deal_cards(players, screen):
    card_scale = 1.3            # Scaling factor of card drawn
    boundary_offset = 0.30      # 30% of screen on both sides
    bottom_offset = 0.05        # 10% of screen from the bottom
    time_between_cards = 50     # In milliseconds
    
    ###### This code segment displays the back of a card at the center of the table, as a prop########
    pygame.display.update()
    card_back = pygame.transform.rotozoom(load_image(card_files()['back - up']), 180, card_scale)
    card_rect = card_back.get_rect()
    card_rect.center = screen.get_rect().center
    screen.blit(card_back, card_rect)
    pygame.display.update(card_rect)
    pygame.time.delay(250)              # Delay before dealing is started
    ##################################################################################################
    
    for player in players:
        if player.index is 1: deal_user_cards(player, screen, card_scale, boundary_offset, bottom_offset, time_between_cards)
        elif player.index is 2: deal_second_player(player, screen, card_scale, boundary_offset, bottom_offset, time_between_cards)
        elif player.index is 3: deal_third_player(player, screen, card_scale, boundary_offset, bottom_offset, time_between_cards)
        elif player.index is 4: deal_fourth_player(player, screen, card_scale, boundary_offset, bottom_offset, time_between_cards)


def deal_user_cards(player, screen, card_scale, boundary_offset, bottom_offset, time_between_cards):
    
    ##########################Load the images, scale and rotate them as required######################
    images = [card.image_file for card in player.hand]
    images = map(load_image, images)
    scale = [card_scale for _ in xrange(len(player.hand))]
    angle = [180 for _ in xrange(len(player.hand))]
    images = map(pygame.transform.rotozoom, images, angle, scale)   # List of images to be blitted
    ##################################################################################################
    
    screen_size = pygame.display.get_surface().get_rect().size
    card_width, card_height = images[0].get_rect().size
    loc = []
    
    ####################################Calculating the x and y positions and increments##############
    x = int(boundary_offset * screen_size[0])
    y = int(screen_size[1] - float(bottom_offset * screen_size[1]) - card_height)
    x_increment = int( float(screen_size[0] * (1 - 2 * boundary_offset) - card_width)/float( len(images) - 1 ) )
    ##################################################################################################
    
    for card in images:
        rect = screen.blit(card, (x, y))
        pygame.display.update(rect)
        loc.append(rect)
        x += x_increment
        pygame.time.delay(time_between_cards)
    
    player.loc = loc    #Adds an attribute loc in the player object which contains rects of all cards
    
    
    
def deal_second_player(player, screen, card_scale, boundary_offset, bottom_offset, time_between_cards):
    
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - side'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    
    ####################################Calculating the x and y positions and increments##############
    x = int(bottom_offset * screen_size[0])
    y = int(boundary_offset * screen_size[1])
    y_increment = int(float(screen_size[1] * (1 - 2 * boundary_offset)-card.get_rect().height)/float(len(player.hand)-1)) 
    ##################################################################################################
        
    for _ in xrange(len(player.hand)):
        pygame.display.update(screen.blit(card, (x, y)))
        y += y_increment
        pygame.time.delay(time_between_cards)

def deal_third_player(player, screen, card_scale, boundary_offset, bottom_offset, time_between_cards):
    
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - up'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    
    ####################################Calculating the x and y positions and increments##############
    x = int(boundary_offset * screen_size[0])
    y = int(bottom_offset * screen_size[1])
    x_increment = int(float(screen_size[0]*(1 - 2 * boundary_offset) - card.get_rect().width)/float(len(player.hand) - 1) )
    ##################################################################################################
    
    for _ in xrange(len(player.hand)):
        pygame.display.update(screen.blit(card, (x, y)))
        x += x_increment
        pygame.time.delay(time_between_cards)
        

def deal_fourth_player(player, screen, card_scale, boundary_offset, bottom_offset, time_between_cards):
    
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - side'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    
    ####################################Calculating the x and y positions and increments##############
    x = int( (1 - bottom_offset) * (screen_size[0]) - card.get_rect().width)
    y = int(boundary_offset * screen_size[1])
    y_increment = int(float(screen_size[1] * (1 - 2 * boundary_offset) - card.get_rect().height)/float(len(player.hand)-1)) 
    ##################################################################################################
    
    for _ in xrange(len(player.hand)):    
        pygame.display.update(screen.blit(card, (x, y)))
        y += y_increment
        pygame.time.delay(time_between_cards)