'''
Created on Jul 14, 2014
@author: Dibyendu
'''
import pygame
from pygame.locals import HWACCEL, SWSURFACE, QUIT, KEYDOWN
from display_engine.methods import load_image
from Classes.humanPlayer import HumanPlayerClass
from Classes.computerPlayer import ComputerPlayerClass
from display_engine import menu_module, deal_module, reset_display, draw_players,\
    draw_selected_cards_module, select_card_module, bidding_module
from Initiate.cardStack import shuffle_deck, split_deck
from display_engine.draw_players import draw_player
from display_engine.blit import static, dynamic
import thread
import threading


class overseer():
    def __init__(self):
        self.images = self.display_init()   # A dictionary which holds a reference to the background and display surfaces
        self.players = self.init_players()  # A list of the four players
        self.status_variables_init()
        
        
    def status_variables_init(self):
        self.running = True                 # While loop condition
        self.status = 'start'               # Event condition
        self.cards = []                     # List of cards
        self.turn = []                      # List of cards played in a round
    
    def display_init(self):
        pygame.init()
        images = {}
        images['screen'] = pygame.display.set_mode((800, 600), HWACCEL | SWSURFACE )
        pygame.display.set_caption("Twenty Nine")
        images['background'] = load_image('table_cloth.jpg', ['images'])
        images['background'] = pygame.transform.scale(images['background'], images['screen'].get_rect().size)
        images['screen'].blit(images['background'], (0, 0))
        pygame.display.flip()
        return images
    
    def shuffle_cards(self, intense = True):
        # intense should be set to True for new game. For new round set it to False
        if intense: return shuffle_deck()
        else: return split_deck(self.cards)
        
    def deal_cards(self):
        self.cards = self.shuffle_cards(intense = True)
        for player in self.players: 
            player.hand = [self.cards.pop(0) for _ in xrange(4)]
            player.sort_hand()
            draw_player(player, self.images['screen'], self.images['background'], time_delay = 50)
        #deal_module.deal_cards(self.players, self.images['screen'])
        self.bidding()
        for player in self.players:
            player.hand += [self.cards.pop(0) for _ in xrange(4)]
            player.sort_hand()
            draw_player(player, self.images['screen'], self.images['background'], time_delay = 50)
        
    def bidding(self):
        t = threading.Thread(target = bidding_module.bidding, args=(self.players, ))
        t.start()
        t.join()
    
    def init_players(self):
        # Creates Players
        return [HumanPlayerClass([] , index, self)if index is 1 else ComputerPlayerClass([], index, self) for index in xrange(1, 5) ]
    
    def menu(self):
        # loads Start Menu
        return menu_module.menu_screen(self.images)
    
    def play_one_turn(self):
        for player in self.players:
            if player.index is not 1: 
                self.turn.append(player.choose_card(self.turn))
                #draw_selected_cards_module.draw_selected_card(player.index, self.images['screen'], self.turn[-1])
                self.render()
                if len(player.hand): # Draws the altered hand only if there's one or more card left
                    draw_players.draw_player(player, self.images['screen'], self.images['background'])
            else:
                choice = player.hand.pop(select_card_module.select_a_card(player, self.images['screen'], self.images['background']))
                self.turn.append(choice)
                #draw_selected_cards_module.draw_selected_card(player.index, self.images['screen'], self.turn[-1])
                self.render()
                print '%s played %s' %(player, choice)
                if len(player.hand): 
                    draw_players.draw_player(player, self.images['screen'], self.images['background'])
            pygame.time.delay(500)
        self.cards += self.turn
        self.turn = []
        print '************************************************'
        return True
    
    def render(self):
        static.blit_background(self.images['screen'], self.images['background'])
        static.blit_middle_deck(self.images['screen'], self.images['background'])
        dynamic.blit_hands(self.players, self.images['screen'], self.images['background'])
        static.blit_turn(self.turn, self.images['screen'], 1.3, 1)
    
    def run(self):
        while self.running:
            if self.status is 'start':
                if self.menu(): self.status = 'deal'
                else: self.running = False
            elif self.status is 'deal':
                self.render()
                self.deal_cards()
                self.status = 'play'
            elif self.status is 'play':
                self.render()
                self.status = 'play' if self.play_one_turn() else 'finish round'
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.running = False