'''
Created on Jul 18, 2014
@author: Dibyendu

Methods to draw the players individually. Can be called by any method to redraw a players hand.
Not to be used for dealing cards animation.
'''
from display_engine.methods import load_image
import pygame
from display_engine.partial_update import get_area_of_player
from display_engine.image_files import card_files

def draw_player(player, screen, background, selected_card_index = 8, raised = False):
    '''This method draws the hands of the players in their positions on the table.
    Set raised to True and provide an index number less than 8 to highlight a selected card.
    Useful to animate card select action by the user!'''
    card_scale = 1.3            # Scaling factor of card drawn
    boundary_offset = 0.30      # 20% of screen on both sides
    bottom_offset = 0.05        # 10% of screen from the bottom
    ##############################################################################################
    if player.index is 1:
        draw_user(player, screen, background, card_scale, boundary_offset, bottom_offset, selected_card_index, raised)
    elif player.index is 2:
        draw_player_2(len(player.hand), screen, background, card_scale, boundary_offset, bottom_offset)
    elif player.index is 3:
        draw_player_3(len(player.hand), screen, background, card_scale, boundary_offset, bottom_offset)
    elif player.index is 4:
        draw_player_4(len(player.hand), screen, background, card_scale, boundary_offset, bottom_offset)
        
        


def draw_user(player, screen, background, card_scale, boundary_offset, bottom_offset, selected_card_index, raised):
    '''Draws the hand of the user in the user's position in the table(bottom)'''
    player_rect = get_area_of_player(1)
    pygame.display.update(screen.blit(background, player_rect, area = player_rect))
    #################################IF there is no card, returns##################################
    if len(player.hand) == 0:
        return
    ################################Loading images#################################################
    images = [card.image_file for card in player.hand]
    images = map(load_image, images)
    scale = [card_scale for _ in xrange(len(images))]
    angle = [180 for _ in xrange(len(images))]
    images = map(pygame.transform.rotozoom, images, angle, scale)
    screen_size = screen.get_rect().size
    card_width, card_height = images[0].get_rect().size
    loc = []
    ########################## If there is only one card, draws it in the center ###################
    if len(images) == 1:
        rect = images[0].get_rect()
        x,y = rect.midtop = (screen.get_rect().centerx, int(screen_size[1] - float(bottom_offset * screen_size[1]) - card_height))
        screen.blit(images[0], rect) if not raised else screen.blit(images[0], (x , y -8))
        loc.append(rect)
        pygame.display.update(loc)
        player.loc = loc
        return
    ################################Calculating x and y coordinates#################################
    x = int(boundary_offset * screen_size[0])
    y = int(screen_size[1] - float(bottom_offset * screen_size[1]) - card_height)
    x_increment = int( float(screen_size[0] * (1 - 2 * boundary_offset) - card_width)/float( len(images) - 1 ) )
    ################################################################################################
    for card, index in zip(images, xrange(len(images))):
        rect = screen.blit(card, (x, y)) if index is not selected_card_index else screen.blit(card, (x, y - 8))
        loc.append(rect)
        x += x_increment
    ###########################Updating Display and replacing list of rects of user#################
    pygame.display.update(loc)
    player.loc = loc
    
    
    
def draw_player_2(number_of_cards, screen, background, card_scale, boundary_offset, bottom_offset):
    player_rect = get_area_of_player(2)
    pygame.display.update(screen.blit(background, player_rect.topleft, area = player_rect))
    ####################################Loading image###############################################
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - side'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    ############################If there is a single cards blits it at the center#####################
    if number_of_cards == 1:
        rect = card.get_rect()
        rect.midleft = ( int(screen.get_rect().width * bottom_offset), screen.get_rect().centery)
        pygame.display.update(screen.blit(card, rect))
        return
    ####################################Calculating the x and y positions and increments############
    x = int(bottom_offset * screen_size[0])
    y = int(boundary_offset * screen_size[1])
    y_increment = int(float(screen_size[1] * (1 - 2 * boundary_offset)-card.get_rect().height)/float(number_of_cards - 1))
    ################################################################################################
    for _ in xrange(number_of_cards):
        pygame.display.update(screen.blit(card, (x, y)))
        y += y_increment
        


def draw_player_3(number_of_cards, screen, background, card_scale, boundary_offset, bottom_offset):
    player_rect = get_area_of_player(3)
    pygame.display.update(screen.blit(background, player_rect.topleft, area = player_rect))
    ####################################### Loading Card Image #####################################
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - up'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    ############################If there is a single cards blits it at the center#####################
    if number_of_cards == 1:
        rect = card.get_rect()
        rect.midtop = ( screen.get_rect().centerx, int(screen.get_rect().height * bottom_offset))
        pygame.display.update(screen.blit(card, rect))
        return
    ####################################Calculating the x and y positions and increments#############
    x = int(boundary_offset * screen_size[0])
    y = int(bottom_offset * screen_size[1])
    x_increment = int(float(screen_size[0]*(1 - 2 * boundary_offset) - card.get_rect().width)/float(number_of_cards - 1) )
    #################################################################################################
    for _ in xrange(number_of_cards):
        pygame.display.update(screen.blit(card, (x, y)))
        x += x_increment
        
        
def draw_player_4(number_of_cards, screen, background, card_scale, boundary_offset, bottom_offset):
    player_rect = get_area_of_player(4)
    pygame.display.update(screen.blit(background, player_rect.topleft, area = player_rect))
    #####################################Loading Card Image##########################################
    screen_size = screen.get_rect().size
    card = load_image(card_files()['back - side'])
    card = pygame.transform.rotozoom(card, 180, card_scale)
    ############################If there is a single cards blits it at the center#####################
    if number_of_cards == 1:
        rect = card.get_rect()
        rect.midright = ( int(screen.get_rect().width * (1 - bottom_offset)), screen.get_rect().centery)
        pygame.display.update(screen.blit(card, rect))
        return
    ####################################Calculating the x and y positions and increments##############
    x = int( (1 - bottom_offset) * (screen_size[0]) - card.get_rect().width)
    y = int(boundary_offset * screen_size[1])
    y_increment = int(float(screen_size[1] * (1 - 2 * boundary_offset) - card.get_rect().height)/float(number_of_cards - 1) )
    ##################################################################################################
    for _ in xrange(number_of_cards):    
        pygame.display.update(screen.blit(card, (x, y)))
        y += y_increment