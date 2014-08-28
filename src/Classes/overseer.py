'''
Created on Jul 14, 2014
@author: Dibyendu
'''
import pygame
import math
from pygame.locals import HWACCEL, SWSURFACE, QUIT, KEYDOWN
from display_engine.methods import load_image
from Classes.humanPlayer import HumanPlayerClass
from Classes.computerPlayer import ComputerPlayerClass
from display_engine import menu_module, deal_module, reset_display, draw_players,\
    draw_selected_cards_module, select_card_module
from Initiate.cardStack import shuffle_deck, split_deck
from display_engine.draw_players import draw_player
from display_engine.blit import static, dynamic
from random import randint


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
        # TODO: Implement bidding
        for player in self.players:
            if player.index != 1:
                self.hand_strength(player.hand,player.index,[2,3])
        return 0
    
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
            pygame.time.delay(500+int(math.pow(0, player.index % 4))*3000)
          
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
                    
    def hand_strength(self,hand,index,set_condition):
        
        cons= {'A': 1.5,
               'K': 0.5, 
               'Q': 0.5,
               'J': 4,
               '10':1,
               '9': 2, 
               '8': 0.5,
               '7': 0.5}
        aggression=randint(-2,2)
        suit=[]         # suit is taken to process the strings of the incoming parameter hand. 
        calculation=0   #total point calculation
        trump_order=[]  
        trump=''
        pair=0
        print index
        for i in range(4):              
            suit.append(str(hand[i]).split(' - '))    # Here 'hand' is processed and ['spade - King'] is seperated into ['spade','King']
        print suit
        for i in range(4):
            calculation+=(cons[suit[i][1]]*sum(x.count(suit[i][0]) for x in suit))      #here calculation is made by using the points chart from 'cons'
            trump_order.append([sum(x.count(suit[i][0]) for x in suit),cons[suit[i][1]]])   #it is then ordered by highest suit(1st priority) and then by trump character
        trump_order.sort()
        for i in range(4):
            if trump_order[3][0]==sum(x.count(suit[i][0]) for x in suit) and trump_order[3][1]== cons[suit[i][1]] : #TRUMP SELECTION----1st checking the highest suit in hand.
                trump=suit[i][0]                                                                                    #(Spade,Spade,Spade,Heart) spade have 3 and hearts have 1.
                print trump                                                                                         #(Spade,Spade,Heart,Heart) in this case their character value(from cons) 
                break                                                                                               #will be checked.and if it is also same.then randomly
        hand_strength=15+int(round(calculation/2.615))
        '''--------------------------------------Logic of Pair-------------------------'''
        
        flag=False
        flag2=False
        pair=0
        for i in range(4):
            if 'K' in suit[i]:
                x=i
                print 'x '+str(x)
                flag=True
            for j in range(4):
                if 'Q' in suit[j]:
                    y=j
                    flag2=True
                    print 'y '+str(y)
                if flag and flag2:
                    if suit[x][0]==suit[y][0]:
                        pair=3
                        break
            if pair==3:
                break
        print pair
        
        '''--------------------------------------End of Logic of Pair-------------------------'''
        
        
        
        '''--------------------------------------Logic of Double-------------------------'''
           
        chances_of_double=20
        for i in range(4):
            chances_of_double+=cons[suit[i][1]]
        chances_of_double=int(round(chances_of_double))
#        print chances_of_double
        our_set=0
        opponent_set=1
        change_in_bid=0
       
        jack_count=sum(x.count('J') for x in suit)
        
        
        if jack_count>=2:
            chances_of_double=(90+(jack_count)**2)
            change_in_bid=randint(-2,-1)
        
        if set_condition[opponent_set] == 4:
            chances_of_double-=50
        elif set_condition[opponent_set] == 5:
            chances_of_double+=100
            change_in_bid=int( round( (set_condition[our_set]+set_condition[opponent_set])/2 ) )
            change_in_bid=+randint(0,2)
        probabilistic_outcome_of_double = self.probabilty(1,100,chances_of_double)

        '''--------------------------------------End of Logic of Double-------------------------'''
        
        final_bid=hand_strength+aggression+change_in_bid+pair
           
        '''--------------------------------------Logic of Seven-------------------------'''
        chances_of_seven=0
        if final_bid-hand_strength>3 and hand_strength<20 :
            chances_of_seven+=(20-hand_strength)*2
        probabilistic_outcome_of_seven = self.probability(1,10,chances_of_seven)
               
        '''--------------------------------------End of Logic of Seven-------------------------'''

        result=[final_bid,trump,probabilistic_outcome_of_double,probabilistic_outcome_of_seven] 
        print result
        print '------------------------------'
        return result
    
    def probability(self,upper_limit,lower_limit,critical_point):   
        if randint(upper_limit,lower_limit) <= critical_point :     
            return True
        else :
            return False