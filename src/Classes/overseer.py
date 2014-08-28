'''
Created on Jul 14, 2014
@author: Dibyendu
'''
import pygame
from pygame.locals import HWACCEL, SWSURFACE
from display_engine.methods import load_image
from Classes.humanPlayer import HumanPlayerClass
from Classes.computerPlayer import ComputerPlayerClass
from display_engine import menu_module, bidding_module, new_round_module
from Initiate.cardStack import shuffle_deck, split_deck
from display_engine.draw_players import draw_player
from display_engine.blit import static, dynamic


class overseer():
    def __init__(self):
        self.images = self.display_init()   # A dictionary which holds a reference to the background and display surfaces
        self.players = self.init_players()  # A list of the four players
        self.status_variables_init()
        self.init_teams()
        
        
    def status_variables_init(self):
        '''Initializes gameplay variables'''
        self.running = True                 # While loop condition
        self.status = 'start'               # Event condition
        self.cards = []                     # List of cards
        self.turn = []                      # List of cards played in a round
        self.trump = None                   # The suit of trump is stored here
        self.max_bidder = None              # Stores reference to the highest bidder
        self.bid = 0                        # Bid for current round
        self.trump_shown = False            # Flag used to keep track if bid has been shown or not
    
    def display_init(self):
        '''Initializes the display variables'''
        pygame.init()
        images = {}
        images['screen'] = pygame.display.set_mode((800, 600), HWACCEL | SWSURFACE )
        pygame.display.set_caption("Twenty Nine")
        images['background'] = load_image('table_cloth_sepia.jpg', ['images'])
        images['background'] = pygame.transform.scale(images['background'], images['screen'].get_rect().size)
        images['screen'].blit(images['background'], (0, 0))
        pygame.display.flip()
        return images
    
    def shuffle_cards(self, intense = True):
        '''Intense should be set to True for new game. For new round set it to False'''
        if intense: return shuffle_deck()
        else: return split_deck(self.cards)
        
    def deal_cards(self):
        '''Deals 4 cards to each player.
           Calls the bidding function. Then deals remaining 4 cards'''
        self.cards = self.shuffle_cards(intense = True)
        for player in self.players: 
            player.hand = [self.cards.pop(0) for _ in xrange(4)]
            player.sort_hand()
            draw_player(player, self.images['screen'], self.images['background'], time_delay = 50)
        if not self.bidding():
            # When all the players pass, cards are dealt again from the start
            self.reset_state()
            return
        for player in self.players:
            player.hand += [self.cards.pop(0) for _ in xrange(4)]
            player.sort_hand()
            draw_player(player, self.images['screen'], self.images['background'], time_delay = 50)
        
    def bidding(self):
        '''Sets the bid, highest bidder and trump variables'''
        self.bid, self.trump, self.max_bidder = bidding_module.bidding(self.players)
        return self.bid and self.trump and self.max_bidder  # Results in False when all are false
    
    def init_players(self):
        '''Creates list of Players'''
        return [HumanPlayerClass(self, index)if index is 1 else ComputerPlayerClass(self, index) for index in xrange(1, 5) ]
    def init_teams(self):
        self.team_a = ['a'] + [player for player in self.players if player.index in (1, 3)] + [0, 0]
        self.team_b = ['b'] + [player for player in self.players if player.index in (2, 4)] + [0, 0]
    
    def menu(self):
        ''' loads Start Menu '''
        return menu_module.menu_screen(self.images)
    
    def new_round(self):
        '''Asks user wether to play another round'''
        return new_round_module.new_round()
    
    def play_one_turn(self):
        return_flag = True      # return flag. Set to False if all cards have been played in a round.
        for player in self.players:
            self.turn.append(player.choose_card(self.turn))
            self.render()
            print ('%s played %s'%(player, self.turn[-1]))
            pygame.time.delay(500)
            if not len(player.hand):
                return_flag = False
        self.cards += self.turn
        self.turn = []
        print '**************End Of Turn***************'
        return return_flag
    
    def score_turn(self):
        pass
    
    def render(self):
        static.blit_background(self.images['screen'], self.images['background'])
        static.blit_middle_deck(self.images['screen'], self.images['background'])
        dynamic.blit_hands(self.players, self.images['screen'], self.images['background'])
        static.blit_turn(self.turn, self.images['screen'], 1.3, 1)
        
    def reset_state(self):
        '''Resets all the state variables of the game.
           Similar to starting a new round. Would not reset scores'''
        for player in self.players:
            self.cards += player.hand
            player.hand[:] = []
        self.status = 'deal'
        self.turn = []
        self.bid = 0
        self.max_bidder = None
        self.trump = None
        self.trump_shown = False
            
    
    def run(self):
        while self.running:
            if self.status is 'start':
                self.running = self.menu()
                self.status = 'deal'
            elif self.status is 'deal':
                self.render()
                self.status = 'play'
                self.deal_cards()
            elif self.status is 'play':
                self.render()
                self.status = 'play' if self.play_one_turn() else 'finish round'
            elif self.status is 'finish round':
                self.render()
                self.status = 'new round'
            elif self.status is 'new round':
                self.running = self.new_round()
                self.status = 'deal'