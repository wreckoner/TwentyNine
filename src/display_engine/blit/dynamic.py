'''
Created on Jul 24, 2014
@author: Dibyendu
'''
from display_engine import draw_players

def blit_hands(players, screen, background):
    for player in players:
        blit_hand(player, screen, background)

def blit_hand(player, screen, background):
    draw_players.draw_player(player, screen, background, selected_card_index = 8, time_delay = 0, raised = False)